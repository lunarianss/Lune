import logging
from typing import Optional

from domain.rag.entity import document, blob
from core.rag.extractor.interface import extractor_base
from core.rag.util.chardet import detect_file_encodings

import pandas as pd


logger = logging.getLogger(__name__)


class CSVExtractor(extractor_base.BaseExtractor):
    def __init__(self, file_path: str,
                 encoding: Optional[str] = None,
                 autodetect_encoding: bool = False,
                 source_column: Optional[str] = None,
                 csv_args: Optional[dict] = None):
        self._file_path = file_path
        self._encoding = encoding
        self._autodetect_encoding = autodetect_encoding
        self.source_column = source_column
        self.csv_args = csv_args or {}

    def extract(self) -> list[document.Document]:
        docs = []
        try:
            with open(self._file_path, newline="", encoding=self._encoding) as csvfile:
                docs = self._read_from_file(csvfile)
        except UnicodeDecodeError as e:
            if self._autodetect_encoding:
                detected_encodings = detect_file_encodings(self._file_path)
                for encoding in detected_encodings:
                    try:
                        with open(self._file_path, newline="", encoding=encoding.encoding) as csvfile:
                            docs = self._read_from_file(csvfile)
                        break
                    except UnicodeDecodeError:
                        continue
            else:
                raise RuntimeError(f"Error loading {self._file_path}") from e

        return docs

    def _read_from_file(self, csv_file) -> list[document.Document]:
        docs = []
        try:
            df = pd.read_csv(csv_file, on_bad_lines="skip", **self.csv_args)

            if self.source_column and self.source_column not in df.columns:
                raise ValueError(
                    f"Source column '{self.source_column}' not found in CSV file.")

            for i, row in df.iterrows():
                content = ";".join(
                    f"{col.strip()}: {str(row[col]).strip()}" for col in df.columns)
                source = row[self.source_column] if self.source_column else ""
                metadata = {"source": source, "row": i}
                doc = document.Document(
                    page_content=content, metadata=metadata)
                docs.append(doc)
        except Exception as e:
            raise e

        return docs
