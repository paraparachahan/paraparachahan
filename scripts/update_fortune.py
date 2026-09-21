from pathlib import Path

readme = Path("README.md").read_text(encoding="utf-8")
fortune = Path("fortune.txt").read_text(encoding="utf-8")

start = "<!-- fortune:start -->"
end = "<!-- fortune:end -->"

before, rest = readme.split(start, 1)
old_message, after = rest.split(end, 1)

new_readme = (
    before
    + start + "\n"
    + fortune.strip() + "\n"
    + end
    + after
)

Path("README.md").write_text(new_readme, encoding="utf-8")

print("READMEを更新しました。")
