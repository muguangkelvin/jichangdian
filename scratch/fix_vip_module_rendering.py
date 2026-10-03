import os
import re

BASE_DIR = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

# 1. Write layouts/services/list.html
list_html_path = os.path.join(BASE_DIR, "layouts", "services", "list.html")
service_layout = """{{ define "main" }}
<div class="service-page-container">
  {{ partial "vip_service_cta.html" . }}

  <div class="container section-padding">
    <div class="service-page-wrapper">
      <div class="service-body">
        {{ .Content }}
      </div>
    </div>
  </div>
</div>
{{ end }}
"""

with open(list_html_path, "w", encoding="utf-8") as f:
    f.write(service_layout)

print("Created layouts/services/list.html")

# 2. Update layouts/services/single.html
single_html_path = os.path.join(BASE_DIR, "layouts", "services", "single.html")
with open(single_html_path, "w", encoding="utf-8") as f:
    f.write(service_layout)

print("Updated layouts/services/single.html")

# 3. Update layouts/index.html (place right at the bottom above {{ end }})
index_path = os.path.join(BASE_DIR, "layouts", "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_text = f.read()

# Remove any existing partial "vip_service_cta.html"
idx_text = idx_text.replace('{{ partial "vip_service_cta.html" . }}\n\n', '').replace('\n\n{{ partial "vip_service_cta.html" . }}', '')

# Insert right above {{ end }} at the end of main
idx_text = idx_text.replace('</section>\n{{ end }}', '</section>\n\n{{ partial "vip_service_cta.html" . }}\n{{ end }}')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_text)

print("Updated layouts/index.html with vip_service_cta.html above footer")

# 4. Update build_all.py to also generate layouts/services/list.html
build_all_path = os.path.join(BASE_DIR, "build_all.py")
with open(build_all_path, "r", encoding="utf-8") as f:
    build_code = f.read()

# Update single.html and list.html write in build_all.py
if 'write_file("layouts/services/list.html"' not in build_code:
    build_code = build_code.replace(
        'write_file("layouts/services/single.html", """',
        'write_file("layouts/services/list.html", """' + service_layout + '""")\nwrite_file("layouts/services/single.html", """'
    )
    with open(build_all_path, "w", encoding="utf-8") as f:
        f.write(build_code)
    print("Updated build_all.py to write layouts/services/list.html")
