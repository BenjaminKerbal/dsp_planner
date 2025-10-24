import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import requests
from slpp import slpp as lua

_HTML_FILE_LOCATION = Path(__file__).parents[2] / "data" / "dsp_recipe_data.html"


@lru_cache
def get_dsp_html() -> str:
    if _HTML_FILE_LOCATION.exists():
        with open(_HTML_FILE_LOCATION, encoding='utf-8') as f:
            return f.read()

    _HTML_FILE_LOCATION.parent.mkdir(parents=True, exist_ok=True)
    url = "https://dyson-sphere-program.fandom.com/wiki/Module:Recipe/Data"
    try:
        html_data = requests.get(url, timeout=60).text
    except requests.Timeout as e:
        raise RuntimeError(f"Request to {url} timed out after 60 seconds") from e
    with open(_HTML_FILE_LOCATION, "w", encoding="utf-8") as f:
        f.write(html_data)
    return html_data


def extract_data(group_name: str) -> Any:
    """
    Extract data group from the dsp wiki html file by first
    isolating the lua table text and then decoding it.
    """

    source = get_dsp_html()
    # find "varname =" then the first '{'
    start = re.search(rf"\b{re.escape(group_name)}\s*=", source)
    if not start:
        raise RuntimeError(f"Couldn't find '{group_name} ='")
    start_index = source.find("{", start.end())
    if start_index == -1:
        raise RuntimeError(f"Couldn't find opening '{{' for {group_name}")

    depth = 0
    end_index = start_index
    while end_index < len(source):
        ch = source[end_index]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end_index += 1
                break
        end_index += 1
    if depth != 0:
        raise RuntimeError(f"Unbalanced braces while reading {group_name}")
    return lua.decode(source[start_index:end_index])
