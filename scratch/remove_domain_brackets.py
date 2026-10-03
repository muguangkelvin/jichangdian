import os
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# Target directories to clean
target_dirs = [
    os.path.join(BASE_DIR, "content"),
    os.path.join(BASE_DIR, "layouts"),
    os.path.join(BASE_DIR, "scratch")
]

# Specific files to clean
target_files = [
    os.path.join(BASE_DIR, "build_all.py"),
    os.path.join(BASE_DIR, "hugo.toml"),
    os.path.join(BASE_DIR, "README.md")
]

for d in target_dirs:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith(('.md', '.html', '.toml', '.py')):
                target_files.append(os.path.join(root, f))

cleaned_count = 0
for filepath in set(target_files):
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    if "" in content or "" in content:
        # Perform replacements
        new_content = content.replace("机场典", "机场典")
        new_content = new_content.replace("机场典", "机场典")
        new_content = new_content.replace("", "")
        new_content = new_content.replace("", "")
        new_content = new_content.replace("", "")
        
        with open(filepath, "w", encoding="utf-8") as f_out:
            f_out.write(new_content)
        cleaned_count += 1

print(f"Successfully cleaned {cleaned_count} files!")
