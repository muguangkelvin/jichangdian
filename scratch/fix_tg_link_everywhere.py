import os
import glob

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"
TG_REAL_URL = "https://t.me/+JngXxDbAxwA5NzVl"

# 1. Update build_all.py
build_all_path = os.path.join(BASE_DIR, "build_all.py")
with open(build_all_path, "r", encoding="utf-8") as f:
    build_code = f.read()

fixed_build_code = build_code.replace("https://t.me/+JngXxDbAxwA5NzVl", TG_REAL_URL)
with open(build_all_path, "w", encoding="utf-8") as f:
    f.write(fixed_build_code)

print("Fixed build_all.py replacement of https://t.me/+JngXxDbAxwA5NzVl")

# 2. Update all files in layouts/, content/, static/, scratch/
search_dirs = [
    os.path.join(BASE_DIR, "layouts"),
    os.path.join(BASE_DIR, "content"),
    os.path.join(BASE_DIR, "scratch")
]

fixed_count = 0
for d in search_dirs:
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(('.html', '.md', '.json', '.toml', '.py')):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if "https://t.me/+JngXxDbAxwA5NzVl" in content:
                    new_content = content.replace("https://t.me/+JngXxDbAxwA5NzVl", TG_REAL_URL)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    fixed_count += 1

print(f"Fixed {fixed_count} template/content files containing {https://t.me/+JngXxDbAxwA5NzVl}")
