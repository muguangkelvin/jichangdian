import os

index_html_path = r"c:\Users\USER\Desktop\博客\jichangdian.xyz\public\index.html"

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "home-guide-article-wrapper"
if start_marker in content:
    idx = content.find(start_marker)
    snippet = content[idx:idx+15000]
    
    forbidden_symbols = ['!', '！', '@', '#', '￥', '%', '……', '&', '*']
    found = [sym for sym in forbidden_symbols if sym in snippet]
    
    print("=== VERIFICATION RESULT ===")
    print("Found home-guide-article-wrapper: YES")
    print("Forbidden symbols count:", len(found))
    print("Forbidden symbols found:", found)
else:
    print("Marker home-guide-article-wrapper NOT found!")
