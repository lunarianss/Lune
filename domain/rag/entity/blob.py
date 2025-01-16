
from pydantic import BaseModel, ConfigDict, model_validator
from typing import Any, Optional, Union
from pathlib import Path, PurePath
from collections.abc import Mapping, Generator, Iterable
from io import BufferedReader, BytesIO

import contextlib


class Blob(BaseModel):
    data: Union[str, bytes, None] = None
    mimetype: Optional[str] = None
    encoding: str = "utf-8"
    path: Optional[Union[str, PurePath]]
    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)

    @property
    def source(self) -> Optional[str]:
        return str(self.path) if self.path else None

    @model_validator(mode="before")
    @classmethod
    def check_blob_is_valid(cls, values: Mapping[str, any]) -> Mapping[str, any]:
        if "data" not in values and "path" not in values:
            raise ValueError("Either data or path must be provided")

        return values

    @contextlib.contextmanager
    def as_bytes_io(self) -> Generator[Union[BytesIO, BufferedReader]]:
        if isinstance(self.data, bytes):
            yield BytesIO(self.data)
        elif self.data is None and self.path:
            with open(str(self.path), "rb") as f:
                yield f
        else:
            raise NotImplementedError(f"Unable to convert blob {self}")
