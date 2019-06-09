from typing import Any, Dict, TextIO, Type

def load(f: TextIO, Loader: Type) -> Dict[Any, Any]: ...

class FullLoader:
    pass
