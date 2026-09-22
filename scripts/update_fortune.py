from pathlib import Path
from html import escape

readme = Path("README.md").read_text(encoding="utf-8")
fortune = Path("fortune.txt").read_text(encoding="utf-8")

start = "<!-- fortune:start -->"
end = "<!-- fortune:end -->"

before, rest = readme.split(start, 1)
old_message, after = rest.split(end, 1)

lines = fortune.strip().splitlines()

# 行頭の空白を除いて「-- 」で始まる行を、作者表記として探す
author_index = None

for index, line in enumerate(lines):
    if line.lstrip().startswith("-- "):
        author_index = index
        break

if author_index is None:
    # 作者表記がない場合
    body = " ".join(fortune.split())
    text = escape(body)
else:
    # 本文と作者表記を、それぞれ1行にまとめる
    body = " ".join(" ".join(lines[:author_index]).split())
    author = " ".join(" ".join(lines[author_index:]).split())

    text = (
    escape(body)
    + '\n\n<p align="right">'
    + escape(author)
    + "</p>"
    )
    
new_readme = (
    before
    + start + "\n\n"
    + text + "\n\n"
    + end
    + after
)

Path("README.md").write_text(new_readme, encoding="utf-8")

print("READMEを更新しました。")
