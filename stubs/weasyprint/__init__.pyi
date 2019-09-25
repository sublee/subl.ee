from typing import BinaryIO, List

from weasyprint.fonts import FontConfiguration

class HTML:
    def __init__(self, string: str) -> None: ...
    def render(self, stylesheets: List[CSS], font_config: FontConfiguration) -> Document: ...

class CSS:
    def __init__(self, string: str, font_config: FontConfiguration) -> None: ...

class Document:
    pages: List[Page]
    def write_pdf(self, f: BinaryIO) -> None: ...

class Page:
    pass
