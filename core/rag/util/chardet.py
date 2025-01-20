from pathlib import Path
from typing import NamedTuple, Optional, cast
import chardet
import concurrent.futures


class FileEncoding(NamedTuple):
    encoding: Optional[str]
    confidence: float
    language: Optional[str]


def detect_file_encodings(file_path: str, timeout: int = 5) -> list[FileEncoding]:
    def read_and_detect(file_path: str) -> list[dict]:
        rawdata = Path(file_path).read_bytes()
        return cast(list[dict], chardet.detect_all(rawdata))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(read_and_detect, file_path)
        try:
            encodings = future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            raise TimeoutError(
                f"Timeout reached while detecting encoding for {file_path}")

    if all(encoding["encoding"] is None for encoding in encodings):
        raise RuntimeError(f"Could not detect encoding for {file_path}")
    return [FileEncoding(**enc) for enc in encodings if enc["encoding"] is not None]
