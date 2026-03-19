# /// script
# requires-python = ">=3.13"
# dependencies = ["beautifulsoup4"]
# ///

from pathlib import Path
import shutil
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "_site"

OUT_DIR.mkdir(exist_ok=True)

tools = []

for tool_dir in sorted(ROOT.iterdir()):
    if not tool_dir.is_dir():
        continue
    if tool_dir.name.startswith((".", "_")):
        continue
    index = tool_dir / "index.html"
    if not index.exists():
        continue

    soup = BeautifulSoup(index.read_text(), "html.parser")
    title = soup.find("title")
    desc = soup.find("meta", attrs={"name": "description"})

    tools.append({
        "slug": tool_dir.name,
        "title": title.get_text(strip=True) if title else tool_dir.name,
        "desc": desc["content"] if desc else "",
    })

    dest = OUT_DIR / tool_dir.name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(tool_dir, dest)

items = []
for tool in tools:
    desc_html = f'\n        <p class="desc">{tool["desc"]}</p>' if tool["desc"] else ""
    items.append(
        f'      <li>\n'
        f'        <a href="/{tool["slug"]}/">{tool["title"]}</a>{desc_html}\n'
        f'      </li>'
    )

tools_list = "\n".join(items)

template = (ROOT / "index.html.template").read_text()
output = template.replace("<!-- TOOLS_LIST -->", tools_list)
(OUT_DIR / "index.html").write_text(output)

print(f"Built {len(tools)} tool(s) → {OUT_DIR}")
