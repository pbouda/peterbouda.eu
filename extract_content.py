import glob
from langdetect import detect

with open("content_eng.md", "w") as out_eng, open("content_deu.md", "w") as out_deu:
    for filepath in sorted(
        glob.glob("content/**/*.md", recursive=True)
        + glob.glob("content/**/*.rst", recursive=True)
    ):
        with open(filepath) as f:
            lines = f.readlines()

        # Extract title and find where content starts
        if filepath.endswith(".md"):
            title = lines[0].replace("Title:", "").strip()
            # Skip metadata lines (key: value format) until empty line
            content_start = (
                next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "") + 1
            )
        else:  # .rst
            title = lines[0].strip()
            # Find first empty line after underline (line 1), content starts after it
            content_start = next(
                i for i, line in enumerate(lines[2:], 2) if line.strip() == ""
            ) + 1

        content = "".join(lines[content_start:])

        # Detect language and write to appropriate file
        try:
            lang = detect(content)
        except:
            lang = "en"  # fallback to English

        output = f"# {title}\n\n{content}\n\n---\n\n"
        if lang == "de":
            print(f"[DE] {filepath}")
            out_deu.write(output)
        else:
            print(f"[EN] {filepath}")
            out_eng.write(output)
