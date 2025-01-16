from core.rag.extractor.interface import extractor_base
from domain.rag.entity import document, blob
from collections.abc import Iterator


class PdfExtractor(extractor_base.BaseExtractor):

    def __init__(self, file_path: str):
        self._file_path = file_path

    def extract(self) -> list[document.Document]:
        pass

    def parse(self, blob: blob.Blob) -> Iterator[document.Document]:
        pass
