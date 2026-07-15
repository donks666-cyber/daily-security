#!/usr/bin/env python3
import os
import xml.etree.ElementTree as ET
from datetime import datetime

BASEDIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTDIR = os.path.join(BASEDIR, 'output')
SITEMAP_FILE = os.path.join(OUTPUTDIR, 'sitemap.xml')
SITEURL = 'https://fsocietys.com'

def build_sitemap():
    urls = []
    for root, dirs, files in os.walk(OUTPUTDIR):
        if 'static' in root or 'feeds' in root:
            continue
        for f in sorted(files):
            if not f.endswith('.html'):
                continue
            filepath = os.path.join(root, f)
            relpath = os.path.relpath(filepath, OUTPUTDIR)
            url = '/' + relpath
            if url.endswith('/index.html'):
                url = url[:-10]
            elif url.endswith('.html'):
                url = url[:-5]
            if url == '/index':
                url = '/'
            urls.append(url)

    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    for url in sorted(urls):
        u = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(u, 'loc')
        loc.text = f'{SITEURL}{url}'

    tree = ET.ElementTree(urlset)
    tree.write(SITEMAP_FILE, encoding='utf-8', xml_declaration=True)
    print(f'[+] Sitemap generated: {SITEMAP_FILE} ({len(urls)} URLs)')

    import shutil
    dest = os.path.join(BASEDIR, 'content', 'sitemap.xml')
    shutil.copy2(SITEMAP_FILE, dest)
    print(f'[+] Copied to {dest}')

if __name__ == '__main__':
    if not os.path.isdir(OUTPUTDIR):
        print('[-] output/ directory not found')
        exit(1)
    build_sitemap()
