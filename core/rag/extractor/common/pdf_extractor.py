from core.rag.extractor.interface import extractor_base
from domain.rag.entity import document, blob
from collections.abc import Iterator

import pypdfium2
import logging


logger = logging.getLogger(__name__)


class PdfExtractor(extractor_base.BaseExtractor):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def extract(self) -> list[document.Document]:
        documents = list(self.load())

        text_list = []
        for document in documents:
            text_list.append(document.page_content)

        text = "\n\n".join(text_list)
        return documents

    def load(self) -> Iterator[document.Document]:
        b = blob.Blob.from_path(self._file_path)

        yield from self.parse(b)

    def parse(self, blob: blob.Blob) -> Iterator[document.Document]:
        with blob.as_bytes_io() as file_obj:
            pdf_reader = pypdfium2.PdfDocument(file_obj, autoclose=True)

            try:
                for page_number, page in enumerate(pdf_reader):
                    text_page = page.get_textpage()
                    content = text_page.get_text_range()
                    text_page.close()
                    page.close()
                    metadata = {"source": blob.source, "page": page_number}
                    yield document.Document(page_content=content, metadata=metadata)
            finally:
                pdf_reader.close()
