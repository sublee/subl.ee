from typing import Callable, Dict, Iterator, TypeVar

from flask import Flask

T = TypeVar('T', bound=Callable[[], Iterator[Dict[str, str]]])

class Freezer:
    def __init__(self, app: Flask, with_static_files: bool) -> None: ...
    def register_generator(self, f: T) -> T: ...
    def freeze(self) -> None: ...
