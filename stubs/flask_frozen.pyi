from typing import Any, Callable, Iterator, TypeVar

from flask import Flask

T = TypeVar('T', bound=Callable[[], Iterator[tuple[str, dict[str, Any]]]])

class Freezer:
    def __init__(self, app: Flask, with_static_files: bool) -> None: ...
    def register_generator(self, f: T) -> T: ...
    def freeze(self) -> None: ...
