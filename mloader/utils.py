import re
import string
from typing import Optional


def is_oneshot(chapter_name: str, chapter_subtitle: str) -> bool:
    for name in (chapter_name, chapter_subtitle):
        name = name.lower()
        if "one" in name and "shot" in name:
            return True
    return False


def chapter_name_to_int(name: str) -> Optional[int]:
    try:
        return int(name.lstrip("#"))
    except ValueError:
        return None


# Capitalize Custom RegEx search result
def bracket_match_capitalize(match):
    return match.group(0).capitalize()


def beautify_path(path: str) -> str:
    # Remove/Replace some blacklisted characters
    clean_str = re.sub(r'[~`!@$^*\\【】]', '', path).replace(': ', " - ").replace(':', "-").replace("/", " of ")
    # Convert everything to list of items
    clean_list = re.findall(r"([\S]+)+", clean_str, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    result = []
    for item in clean_list:
        # Capitalize first characters inside enclosing brackets
        item = re.sub(r'\((.*?)\)|\[(.*?)\]|\{(.*?)\}', bracket_match_capitalize, item)
        # Capitalize word if has apostrophe, else make Title case
        item = ' '.join(word.capitalize() if "'" in word else word.title() for word in item.split())
        result.append(item)
    # Put back the newly formatted items as string
    return ' '.join(result)
