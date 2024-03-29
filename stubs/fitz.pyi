class Pixmap:
    def tobytes(self) -> bytes: ...

class Page:
    def get_pixmap(self, dpi: int) -> Pixmap: ...

class Document:
    def __getitem__(self, i: int) -> Page: ...

def open(filetype: str, data: bytes) -> Document: ...
