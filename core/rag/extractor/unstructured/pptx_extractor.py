from core.rag.extractor.interface import extractor_base
from domain.rag.entity import document
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.utils import BackoffStrategy, RetryConfig

import os
import logging


logger = logging.getLogger(__name__)


class UnstructuredPPTXExtractor(extractor_base.BaseExtractor):
    def __init__(self, file_path: str, api_url: str, api_key: str):
        self._file_path = file_path
        self._api_url = api_url
        self._api_key = api_key

    def extract(self) -> list[document.Document]:
        documents = []
        text_by_page = {}
        with UnstructuredClient(server_url="localhost:8000") as unstructured_client:
            res = unstructured_client.general.partition(request={
                "partition_parameters": {
                    "files": {
                        "content": open(self._file_path, "rb"),
                        "file_name": os.path.basename(self._file_path),
                    },
                },
            }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

            assert res.elements is not None

            for element in res.elements:
                page = element["metadata"]["page_number"]
                text = element["text"]
                if page in text_by_page:
                    text_by_page[page] += "\n" + text
                else:
                    text_by_page[page] = text

            combined_texts = list(text_by_page.values())
            documents = []
            for combined_text in combined_texts:
                text = combined_text.strip()
                documents.append(document.Document(page_content=text))
            return documents
