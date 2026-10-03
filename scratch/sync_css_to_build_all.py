import os
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"
style_css_path = os.path.join(BASE_DIR, "static", "css", "style.css")
build_all_path = os.path.join(BASE_DIR, "build_all.py")

with open(style_css_path, "r", encoding="utf-8") as f:
    full_css = f.read()

with open(build_all_path, "r", encoding="utf-8") as f:
    build_code = f.read()

# Replace css_content = """...""" in build_all.py
pattern = r'css_content = """(.*?)"""\nwrite_file\("static/css/style\.css", css_content\)'
replacement = 'css_content = """' + full_css.replace('\\', '\\\\') + '"""\nwrite_file("static/css/style.css", css_content)'

new_build_code = re.sub(pattern, replacement, build_code, flags=re.DOTALL)

with open(build_all_path, "w", encoding="utf-8") as f:
    f.write(new_build_code)

print("Successfully synced static/css/style.css into build_all.py!")
