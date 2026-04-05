#rule_loader.py
# Import json to read and parse JSON files such as rules.json

import json  # json is a standard library module for working with JSON data
# Import Path from pathlib to handle file paths in an OS-independent way
from pathlib import Path  # pathlib is a standard library module for filesystem paths
# Import typing utilities for type hints
from typing import List, Dict, Any  # typing is a standard library module for type hints


# Define a function to load rules from a JSON file
def load_rules_from_file(file_path: str) -> List[Dict[str, Any]]:
    # Convert the string file path into a Path object for safer path handling
    path = Path(file_path)

    # Open the file in read mode with UTF-8 encoding
    with path.open("r", encoding="utf-8") as f:
        # Use json.load to parse the JSON content into Python objects (list/dict)
        rules = json.load(f)

    # Return the parsed rules to the caller
    return rules
