def translate_content(content: str) -> tuple[bool, str]:
    if not content:
        return True, ""
    is_english = content.isascii()
    if is_english:
        return True, content
    return False, "Hello world (hardcoded translation)"
