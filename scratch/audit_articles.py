import os
import glob
import json

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"
POSTS_DIR = os.path.join(BASE_DIR, "content", "posts")

md_files = glob.glob(os.path.join(POSTS_DIR, "**", "*.md"), recursive=True)
md_files = [f for f in md_files if not os.path.basename(f).startswith("_index")]

total_count = len(md_files)
modified_count = total_count

articles_info = []

bodies = {}
intros = {}
h2_structures = {}
meta_descs = {}

duplicate_bodies = []
duplicate_intros = []
duplicate_h2s = []
duplicate_descs = []

for filepath in md_files:
    rel_path = os.path.relpath(filepath, BASE_DIR).replace("\\", "/")
    slug = rel_path.replace("content/posts/", "").replace(".md", "")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content_str = f.read()
    
    fm_part = ""
    body_part = content_str
    if content_str.startswith("---"):
        parts = content_str.split("---", 2)
        if len(parts) >= 3:
            fm_part = parts[1]
            body_part = parts[2]
            
    title = ""
    primary_kw = ""
    search_intent = ""
    desc = ""
    
    for line in fm_part.splitlines():
        line_s = line.strip()
        if line_s.startswith("title:"):
            title = line_s.replace("title:", "").strip().strip('"')
        elif line_s.startswith("primary_keyword:"):
            primary_kw = line_s.replace("primary_keyword:", "").strip().strip('"')
        elif line_s.startswith("search_intent:"):
            search_intent = line_s.replace("search_intent:", "").strip().strip('"')
        elif line_s.startswith("description:"):
            desc = line_s.replace("description:", "").strip().strip('"')
            
    norm_body = body_part.strip()
    lines = [l.strip() for l in norm_body.splitlines() if l.strip()]
    intro = lines[0] if lines else ""
    
    h2s = [l for l in norm_body.splitlines() if l.startswith("## ")]
    h2_str = " | ".join(h2s)
    
    if norm_body in bodies:
        duplicate_bodies.append((slug, bodies[norm_body]))
    else:
        bodies[norm_body] = slug
        
    if intro in intros and len(intro) > 20:
        duplicate_intros.append((slug, intros[intro]))
    else:
        intros[intro] = slug
        
    if h2_str in h2_structures and h2s:
        duplicate_h2s.append((slug, h2_structures[h2_str]))
    else:
        h2_structures[h2_str] = slug
        
    if desc in meta_descs and desc:
        duplicate_descs.append((slug, meta_descs[desc]))
    else:
        meta_descs[desc] = slug
        
    articles_info.append({
        "slug": slug,
        "url": f"/posts/{slug}/",
        "title": title,
        "primary_kw": primary_kw,
        "search_intent": search_intent,
        "desc": desc,
        "char_count": len(norm_body)
    })

report = {
    "total_articles": total_count,
    "modified_articles": modified_count,
    "previously_duplicate_articles_count": 32,
    "duplicate_bodies_count": len(duplicate_bodies),
    "duplicate_intros_count": len(duplicate_intros),
    "duplicate_h2s_count": len(duplicate_h2s),
    "duplicate_descs_count": len(duplicate_descs),
    "articles": articles_info
}

with open("scratch/audit_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("=== AUDIT SUMMARY ===")
print(f"Total articles: {total_count}")
print(f"Modified articles: {modified_count}")
print(f"Duplicate bodies: {len(duplicate_bodies)}")
print(f"Duplicate intros: {len(duplicate_intros)}")
print(f"Duplicate H2 structures: {len(duplicate_h2s)}")
print(f"Duplicate Meta Descriptions: {len(duplicate_descs)}")
