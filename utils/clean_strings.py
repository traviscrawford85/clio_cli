# A helper function to clean and sanitize strings, removing invalid characters
# utils/clean_strings.py
def safe_unicode(text: str) -> str:
    # Remove surrogates and replace invalid characters
    return text.encode("utf-8", "replace").decode("utf-8")
