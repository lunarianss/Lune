from core.rag.extractor.interface import extractor_base
from domain.rag.entity import document
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.utils import BackoffStrategy, RetryConfig

import os
import logging


logger = logging.getLogger(__name__)


class UnstructuredHTMLExtractor(extractor_base.BaseExtractor):
    def __init__(self, file_path: str, api_url: str, api_key: str):
        self._file_path = file_path
        self._api_url = api_url
        self._api_key = api_key

    def extract(self) -> list[document.Document]:
        documents = []
        with UnstructuredClient(server_url="localhost:8000") as unstructured_client:
            res = unstructured_client.general.partition(request={
                "partition_parameters": {
                    "files": {
                        "content": open(self._file_path, "rb"),
                        "file_name": os.path.basename(self._file_path),
                    },
                    "chunking_strategy": shared.ChunkingStrategy.BY_TITLE,
                    "strategy": shared.Strategy.HI_RES,
                    "max_characters": 2000,
                    "combine_under_n_chars": 2000,
                },
            }, retries=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

            assert res.elements is not None

            for chunk in res.elements:
                text = chunk["text"].strip()
                documents.append(document.Document(page_content=text))

            return documents
