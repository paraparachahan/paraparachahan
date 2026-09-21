from pathlib import Path
from html import escape

readme = Path("README.md").read_text(encoding="utf-8")
fortune = Path("fortune.txt").read_text(encoding="utf-8")

start = "<!-- fortune:start -->"
end = "<!-- fortune:end -->"

before, rest = readme.split(start, 1)
old_message, after = rest.split(end, 1)

text = " ".join(fortune.split())

new_readme = (
    before
    + start + "\n\n"
    + escape(text) + "\n\n"
    + end
    + after
)

Path("README.md").write_text(new_readme, encoding="utf-8")

print("READMEを更新しました。")
