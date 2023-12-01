"""

Note: Documentation automatically generated by https://undoc.ai
"""
import os
import re


def find_image_path(text):
    """
    def find_image_path(text):
        "/**
        Searches for the longest existing image file path within a given text.
        This function interprets a string of text, looking for patterns that represent
        file paths to image files. It supports both Windows-style and Unix-style paths, and
        looks for common image file extensions (png, jpg, jpeg) in various casings.
        It returns the longest path that actually points to an existing file.
        Args:
            text (str): A string containing potential file paths.
        Returns:
            str or None: The longest existing image file path found in `text`, or `None` if no
            existing file paths are found.
        Note:
            This function does not verify whether the path points to a valid image file;
            it only checks for the existence of the file at the given path.
        ""
        pass
    """
    pattern = r"([A-Za-z]:\\[^:\n]*?\.(png|jpg|jpeg|PNG|JPG|JPEG))|(/[^:\n]*?\.(png|jpg|jpeg|PNG|JPG|JPEG))"
    matches = [match.group() for match in re.finditer(pattern, text) if match.group()]
    matches += [match.replace("\\", "") for match in matches if match]
    existing_paths = [match for match in matches if os.path.exists(match)]
    return max(existing_paths, key=len) if existing_paths else None
