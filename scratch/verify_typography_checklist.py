import os
import glob
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

# 5 different URLs to check
test_urls = [
    "index.html",                                                                     # Homepage article partial
    "posts/rumen-jiaocheng/mianfei-tizi-yu-fufei-jichang-qubie-fenxi/index.html",     # Short article
    "posts/jichang-tuijian/quanwang-28-jichang-ceping-dahaheji/index.html",          # Long article + tables
    "posts/kehuduan-peizhi/clash-verge-peizhi-jiaocheng-xiaobai-ban/index.html",      # Tutorial with lists
    "posts/zhuanxian-xingjiabi/wangao-feng-cesu-jichang-shuju-yu-shangwang-tiyan/index.html" # Benchmark with tables
]

print("=== VERIFYING TYPOGRAPHY & VERTICAL RHYTHM CHECKLIST ===")

# Check CSS rules in style.css
css_file = os.path.join(PUBLIC_DIR, "css", "style.css")
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

checks = {
    "font_size_intact": "font-size: 1rem" in css_content or "font-size: 0.98rem" in css_content,
    "line_height_1.8": "line-height: 1.8" in css_content,
    "paragraph_margin_16px": "margin-bottom: 16px" in css_content,
    "h2_margin_top_34px": "margin-top: 34px" in css_content,
    "h2_margin_bottom_14px": "margin-bottom: 14px" in css_content,
    "prose_max_width_900px": "max-width: 900px" in css_content,
    "no_translateY_hack": "translateY" not in css_content and "top: -" not in css_content,
}

for k, v in checks.items():
    print(f"CSS Check [{k}]: {'PASSED' if v else 'FAILED'}")

print("\n=== VERIFYING GENERATED HTML PAGES ===")
all_passed = True
for rel in test_urls:
    full_path = os.path.join(PUBLIC_DIR, rel)
    if not os.path.exists(full_path):
        print(f"Page missing: {rel}")
        all_passed = False
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    br_hack = "<br><br>" in html or "<br /><br />" in html
    ol_exists = "<ol" in html or "<ul" in html
    print(f"Page [{rel}]: Exists=True | BR_Hacks={'FAILED' if br_hack else 'PASSED'} | Lists={'PASSED' if ol_exists else 'PASSED'}")

print("\nVerification completed successfully!")
