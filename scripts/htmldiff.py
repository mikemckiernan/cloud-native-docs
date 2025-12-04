from bs4 import BeautifulSoup, Tag
from difflib import unified_diff
import re
import argparse

def normalize_html(html_path):
    with open(html_path) as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    for tag in soup(['script', 'style', 'meta', 'head']):
        tag.decompose()

    for element in soup.descendants:
        if not isinstance(element, Tag):
            continue
        for attr in ["lang", "title"]:
          if element.get(attr):
            del element[attr]

    # Normalize whitespace
    text = soup.prettify()
    text = re.sub(r'\n\s*\n', '\n', text)

    return text.splitlines()

def compare_html(old_path, new_path):
    old = normalize_html(old_path)
    new = normalize_html(new_path)

    diff = list(unified_diff(old, new, lineterm=''))

    if not diff:
        return "identical"
    return diff

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_html", type=str)
    parser.add_argument("new_html", type=str)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    old_path = args.old_html
    new_path = args.new_html
    diff = compare_html(old_path, new_path)
    for line in diff:
        print(line)