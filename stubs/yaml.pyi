from typing import Any, Dict, TextIO, Type

def load(f: TextIO, Loader: Type[object]) -> Dict[Any, Any]: ...

class FullLoader:
    pass
