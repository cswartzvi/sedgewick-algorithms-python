from __future__ import annotations
import sys
from typing import Iterable, Iterator


class Reader:
    """This class provides methods for reading strings, numbers and
    boolean from file inputs and standard input.
    """

    def __init__(self, stream: Iterable[str]):
        self._stream = stream

    @classmethod
    def from_file(cls, file: str) -> Reader:
        return cls(open(file, "rt"))

    @classmethod
    def from_stdin(cls) -> Reader:
        return cls(sys.stdin)

    def read_as_bool(self) -> Iterator[bool]:
        yield from (bool(item) for item in self._read())

    def read_as_float(self) -> Iterator[float]:
        yield from (float(item) for item in self._read())

    def read_as_int(self) -> Iterator[int]:
        yield from (int(item) for item in self._read())

    def read_as_strings(self) -> Iterator[str]:
        yield from (item for item in self._read())

    def _read(self) -> Iterator[str]:
        for line in self._stream:
            yield line
