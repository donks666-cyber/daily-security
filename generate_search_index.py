#!/usr/bin/env python3
"""Generate stork search index for the daily-security blog."""
import os
import subprocess
import sys
import re

BASEDIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTDIR = os.path.join(BASEDIR, 'output')
INDEX_FILE = os.path.join(OUTPUTDIR, 'search-index.st')
CONFIG_FILE = os.path.join(BASEDIR, 'stork-config.toml')

def extract_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(2000)
            m = re.search(r'<title>([^<]+)</title>', content)
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return os.path.basename(filepath).replace('.html', '').replace('index', '')

def generate_config():
    config_lines = [
        '[input]',
        f'base_directory = "{OUTPUTDIR}"',
        '',
    ]

    for root, dirs, files in os.walk(OUTPUTDIR):
        if 'static' in root or 'feeds' in root:
            continue
        for f in sorted(files):
            if f.endswith('.html'):
                filepath = os.path.join(root, f)
                relpath = os.path.relpath(filepath, OUTPUTDIR)
                url = '/' + relpath
                if url.endswith('/index.html'):
                    url = url[:-10]
                elif url.endswith('.html'):
                    url = url[:-5]

                # Only index actual article pages and standalone pages
                # Skip listing pages: index, archives, categories, tags, authors, category/*, tag/*, author/*
                skip = False
                if relpath in ('index.html', 'archives.html', 'categories.html', 'tags.html', 'authors.html'):
                    skip = True
                elif relpath.startswith('category/') or relpath.startswith('tag/') or relpath.startswith('author/'):
                    skip = True
                elif not relpath.startswith('posts/'):
                    skip = True
                if skip:
                    continue

                title = extract_title(filepath)

                config_lines.append('[[input.files]]')
                config_lines.append(f'  title = "{title}"')
                config_lines.append(f'  url = "{url}"')
                config_lines.append(f'  path = "{relpath}"')
                config_lines.append('')

    with open(CONFIG_FILE, 'w') as f:
        f.write('\n'.join(config_lines))

    page_count = config_lines.count('[[input.files]]')
    print(f"[+] Generated stork config with {page_count} pages")
    return page_count

def build_index():
    try:
        result = subprocess.run(
            ['stork', 'build', '--input', CONFIG_FILE, '--output', INDEX_FILE],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"[+] Stork search index built: {INDEX_FILE}")
        else:
            print(f"[-] Stork build failed: {result.stderr}")
            print("[!] Install stork: https://github.com/jameslittle230/stork/releases")
            return False
    except FileNotFoundError:
        print("[!] stork binary not found.")
        print("[!] Install: https://github.com/jameslittle230/stork/releases")
        return False
    return True

def copy_to_content():
    import shutil
    dest = os.path.join(BASEDIR, 'content', 'search-index.st')
    shutil.copy2(INDEX_FILE, dest)
    print(f"[+] Copied to {dest}")

if __name__ == '__main__':
    if not os.path.isdir(OUTPUTDIR):
        print("[-] output/ directory not found. Run 'make html' first.")
        sys.exit(1)
    generate_config()
    if build_index():
        copy_to_content()
