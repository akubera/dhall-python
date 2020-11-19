# pyright: strict

# based on github.com/python/typeshed/blob/master/stdlib/3/json/__init__.pyi

from typing import IO, Any, Protocol, TypeVar, Union

_T_co = TypeVar("_T_co", covariant=True)

class SupportsRead(Protocol[_T_co]):
    def read(self, __length: int = ...) -> _T_co: ...

def dumps(obj: Any) -> str: ...
def dump(obj: Any, fp: IO[str]) -> None: ...
def loads(s: Union[str, bytes]) -> Any: ...
def load(fp: SupportsRead[Union[str, bytes]]) -> Any: ...