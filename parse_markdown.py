import sys
from pathlib import Path
from typing import Any, Dict, List
import re


def split_markdown_by_headings(markdown_text: str, heading_level: int = 1) -> List[str]:
    """
    Split markdown text into sections based on headings of the same level.

    Args:
        markdown_text (str): The markdown text to split
        heading_level (int): The heading level to split on (1 for #, 2 for ##, etc.)

    Returns:
        List[str]: List of markdown sections, each starting with a heading
    """
    # Create the heading pattern based on the specified level
    heading_marker = "#" * heading_level
    pattern = f"^{heading_marker}\\s+.*$"

    # Find all positions where headings occur
    sections = []
    current_section = []

    for line in markdown_text.split("\n"):
        # Check if this line is a heading of the specified level
        if re.match(pattern, line, re.MULTILINE):
            # If we have content in the current section, save it
            if current_section:
                sections.append("\n".join(current_section))
            # Start a new section with this heading
            current_section = [line]
        else:
            current_section.append(line)

    # Add the last section if it exists
    if current_section:
        sections.append("\n".join(current_section))

    return sections


def split_markdown_to_dict(
    markdown_text: str, heading_level: int = 1
) -> Dict[str, str]:
    """
    Split markdown text into a dictionary where keys are heading titles and values are section contents.

    Args:
        markdown_text (str): The markdown text to split
        heading_level (int): The heading level to split on (1 for #, 2 for ##, etc.)

    Returns:
        Dict[str, str]: Dictionary mapping heading titles to section contents
    """
    sections = split_markdown_by_headings(markdown_text, heading_level)
    result = {}

    for section in sections:
        lines = section.split("\n")
        if lines:
            # Extract the heading title (remove #s and whitespace)
            heading = lines[0].lstrip("#").strip()
            # Join the remaining lines as content
            result[heading] = section

    return result


def save_api_reference_result(text: str):
    root_dir = Path("salesforce")
    root_dir.mkdir(exist_ok=True)

    heading2 = split_markdown_to_dict(text, heading_level=2)
    example_header = "CHAPTER 3 Examples"
    examples = heading2[example_header]
    example_dir = root_dir / "examples"
    example_dir.mkdir(exist_ok=True)

    example_components = split_markdown_to_dict(examples, heading_level=3)
    for key, value in example_components.items():
        if key == example_header:
            continue
        with open(example_dir / f"{key}.md", "w") as f:
            f.write(value)

    reference_header = "CHAPTER 5 Reference"
    references = heading2[reference_header]
    reference_dir = root_dir / "references"
    reference_dir.mkdir(exist_ok=True)

    reference_components = split_markdown_to_dict(references, heading_level=3)
    for key, value in reference_components.items():
        if key == reference_header:
            continue
        with open(reference_dir / f"{key}.md", "w") as f:
            f.write(value)

def save_object_reference_result(text: str):
    root_dir = Path("salesforce")
    root_dir.mkdir(exist_ok=True)

    heading3 = split_markdown_to_dict(text, heading_level=3)
    s_object_header = "CHAPTER 6 Standard Objects"
    s_objects = heading3[s_object_header]
    s_object_dir = root_dir / "standard_objects"
    s_object_dir.mkdir(exist_ok=True)

    s_object_components = split_markdown_to_dict(s_objects, heading_level=4)
    for key, value in s_object_components.items():
        if key == s_object_header:
            continue
        with open(s_object_dir / f"{key}.md", "w") as f:
            f.write(value)

# Example usage
if __name__ == "__main__":
    file_path = Path(sys.argv[1])
    with open(file_path, "r") as f:
        markdown_text = f.read()

    if file_path.stem.startswith("salesforce_api_reference"):
        save_api_reference_result(markdown_text)

    if file_path.stem.startswith("salesforce_object_reference"):
        save_object_reference_result(markdown_text)
