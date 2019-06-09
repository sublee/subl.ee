from typing import BinaryIO, List

from weasyprint.fonts import FontConfiguration

class HTML:
    def __init__(self, string: str) -> None: ...
    def write_pdf(self, f: BinaryIO, stylesheets: List[CSS], font_config: FontConfiguration) -> None: ...

class CSS:
    def __init__(self, string: str, font_config: FontConfiguration) -> None: ...
