import re
from typing import Any


def get_file_id(data: str) -> tuple[Any, bool]:
    """
        Extracts a file ID from an HTML-like string.

        Args:
            data (str): The input string potentially containing a file reference.

        Returns:
            tuple[Any, bool]: A tuple containing either the extracted file ID (if found) or the original data,
                              and a boolean indicating whether the data is an image (True if file ID found, False otherwise).
    """
    match = re.search(r'src="([^"]+)"', data) # Search for src attribute containing a file URL
    if match:
        return match.group(1), True # Return extracted file ID and True indicating an image
    else:
        return data, False # Return original data and False indicating no image