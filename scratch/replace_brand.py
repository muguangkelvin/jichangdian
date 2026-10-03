import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\USER\Desktop\博客\jichangdian.xyz"

extensions = ['.html', '.md', '.toml', '.json', '.py', '.txt', '.csv']
ignore_dirs = ['.git', 'public', 'node_modules', '.gemini', 'scratch']

count = 0
files_modified = 0

for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for f in files:
        if any(f.endswith(ext) for ext in extensions):
            full_path = os.path.join(root, f)
            try:
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                if '机场店' in content:
                    occurrences = content.count('机场店')
                    new_content = content.replace('机场店', '机场典')
                    with open(full_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    count += occurrences
                    files_modified += 1
                    print(f"Updated {f}: {occurrences} replacements")
            except Exception as e:
                print(f"Error processing {f}: {e}")

print(f"Total replacements: {count} across {files_modified} files.")
