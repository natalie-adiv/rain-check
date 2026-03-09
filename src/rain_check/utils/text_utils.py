def fix_hebrew(text: str) -> str:
    """Prepends a Right-to-Left (RTL) mark to the text for correct display."""
    return f"\u200f{text}"