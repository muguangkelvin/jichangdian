import re

with open("scratch/generate_rich_articles.py", "r", encoding="utf-8") as f:
    content = f.read()

keys = re.findall(r'"(content/posts/[^"]+)":', content)
print(f"Total keys found: {len(keys)}")
for k in keys:
    print(" -", k)
