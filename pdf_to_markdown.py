import pymupdf4llm
from pathlib import Path
import sys

file_path = Path(sys.argv[1])
md_text = pymupdf4llm.to_markdown(file_path)
with open("output.md", "w") as f:
    f.write(md_text)
