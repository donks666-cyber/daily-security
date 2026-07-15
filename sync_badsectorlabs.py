import os
import re
import sys
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://blog.badsectorlabs.com"
OUTPUT_DIR = "content/posts"
REQUEST_DELAY = 1
MAX_PAGES = 100

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
})
session.verify = False


def safe(text):
    return text.encode('ascii', errors='replace').decode('ascii')


def fetch_soup(url):
    resp = session.get(url, timeout=60)
    resp.raise_for_status()
    # Use raw bytes and let BeautifulSoup detect encoding from <meta charset>
    return BeautifulSoup(resp.content, "html.parser")


def extract_articles_from_index(soup):
    articles = []
    for article_tag in soup.find_all("article"):
        h1 = article_tag.find("h1")
        if not h1:
            continue
        a = h1.find("a")
        if not a:
            continue
        url = a.get("href", "")
        time_tag = a.find("time")
        if not time_tag:
            continue
        date_str = time_tag.get("datetime")
        if not date_str:
            continue
        date = datetime.fromisoformat(date_str)
        # title is text after <time>, not including the time element
        time_tag.extract()
        title_text = a.get_text(strip=True)

        # summary is the <p> right after </h1>; keep HTML for @ links
        summary_p = h1.find_next_sibling("p")
        summary = summary_p.decode_contents().strip() if summary_p else ""

        footer = article_tag.find("footer")
        category = ""
        tags = []
        author = ""
        if footer:
            cat_a = footer.find("a", href=re.compile(r"/category/"))
            if cat_a:
                category = cat_a.get_text(strip=True)
            for tag_a in footer.find_all("a", href=re.compile(r"/tag/")):
                tags.append(tag_a.get_text(strip=True))
            author_a = footer.find("a", href=re.compile(r"/author/"))
            if author_a:
                author = author_a.get_text(strip=True)

        slug_match = re.search(r"/([^/]+)\.html", url)
        slug = slug_match.group(1) if slug_match else ""
        full_url = url if url.startswith("http") else BASE_URL + url
        articles.append(dict(
            url=full_url, title=title_text, date=date,
            summary=summary, category=category, tags=tags,
            author=author, slug=slug
        ))
    return articles


def fetch_all_articles():
    all_articles = []
    for page in range(1, MAX_PAGES + 1):
        url = BASE_URL + "/" if page == 1 else f"{BASE_URL}/index{page}.html"
        print(f"[index] {safe(url)}")
        try:
            soup = fetch_soup(url)
        except requests.RequestException as e:
            print(f"  Error (likely last page): {e}")
            break
        articles = extract_articles_from_index(soup)
        if not articles:
            break
        all_articles.extend(articles)
        print(f"  -> {len(articles)} articles")
        if "older articles" not in soup.get_text():
            break
        time.sleep(REQUEST_DELAY)
    return all_articles


def fetch_content(soup):
    from bs4 import Comment, NavigableString
    start = soup.find(string=lambda s: isinstance(s, Comment) and s.strip() == "content")
    if not start:
        return ""
    parent = start.parent
    children = list(parent.children)
    start_idx = children.index(start)
    parts = []
    for i in range(start_idx + 1, len(children)):
        child = children[i]
        if isinstance(child, Comment) and "/content" in str(child):
            return "\n".join(parts).strip()
        if isinstance(child, NavigableString) and not child.strip():
            continue  # skip whitespace-only strings
        parts.append(str(child))
    return "\n".join(parts).strip()


def write_article(art, content_html):
    filename = f"{art['slug']}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        print(f"  SKIP (exists): {filename}")
        return
    tags_str = ", ".join(art["tags"])
    summary = re.sub(r'\s+', ' ', art['summary']).strip()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Title: {art['title']}\n")
        f.write(f"Date: {art['date'].strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Category: {art['category']}\n")
        if tags_str:
            f.write(f"Tags: {tags_str}\n")
        f.write(f"Slug: {art['slug']}\n")
        f.write(f"Author: {art['author']}\n")
        f.write(f"Summary: {summary}\n")
        f.write("\n")
        f.write(content_html)
        f.write("\n")
    print(f"  OK: {filename}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("Step 1: Discover all article URLs from paginated index")
    print("=" * 60)
    articles = fetch_all_articles()
    print(f"\nTotal articles discovered: {len(articles)}\n")

    print("=" * 60)
    print("Step 2: Fetch full content for each article")
    print("=" * 60)
    for i, art in enumerate(articles, 1):
        print(f"[{i}/{len(articles)}] {safe(art['title'])}")
        try:
            soup = fetch_soup(art["url"])
        except requests.RequestException as e:
            print(f"  Error: {e}")
            time.sleep(REQUEST_DELAY)
            continue
        content = fetch_content(soup)
        if content:
            write_article(art, content)
        else:
            print(f"  ERROR: no content block found")
        time.sleep(REQUEST_DELAY)

    print("\nDone!")


if __name__ == "__main__":
    main()
