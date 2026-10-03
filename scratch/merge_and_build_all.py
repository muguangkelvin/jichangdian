import os
import json
import subprocess
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

with open(os.path.join(BASE_DIR, "scratch/temp_channels_1_2.json"), "r", encoding="utf-8") as f:
    c12 = json.load(f)

with open(os.path.join(BASE_DIR, "scratch/temp_channels_3_4.json"), "r", encoding="utf-8") as f:
    c34 = json.load(f)

ALL_32_ARTICLES = {}
ALL_32_ARTICLES.update(c12)
ALL_32_ARTICLES.update(c34)

print(f"Merged total articles: {len(ALL_32_ARTICLES)}")

# Write all 32 markdown files
written_count = 0
for rel_path, item in ALL_32_ARTICLES.items():
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    fm = f"""---
title: "{item['title']}"
date: 2026-10-02
categories: ["{item['cat']}"]
tags: {json.dumps(item['secondary_kws'], ensure_ascii=False)}
primary_keyword: "{item['primary_kw']}"
secondary_keywords: {json.dumps(item['secondary_kws'], ensure_ascii=False)}
search_intent: "{item['intent']}"
description: "{item['desc']}"
keywords: {json.dumps([item['primary_kw']] + item['secondary_kws'], ensure_ascii=False)}
---

{item['content'].strip()}
"""
    with open(full_path, "w", encoding="utf-8") as f_out:
        f_out.write(fm)
    written_count += 1

print(f"Successfully wrote {written_count} unique markdown files.")

# Also generate scratch/all_articles_dataset.py for build_all.py integration
py_content = "ALL_32_ARTICLES = " + json.dumps(ALL_32_ARTICLES, ensure_ascii=False, indent=4)
with open(os.path.join(BASE_DIR, "scratch/all_articles_dataset.py"), "w", encoding="utf-8") as f_py:
    f_py.write(py_content)

print("Saved scratch/all_articles_dataset.py successfully.")
