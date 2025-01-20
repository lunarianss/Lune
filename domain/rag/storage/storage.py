from domain.rag.storage.interface.base import BaseStorage
from domain.rag.storage.entity.storage_type import StorageType
from collections.abc import Generator
from typing import Union

import logging

logger = logging.getLogger(__name__)


class Storage:
    def __init__(self):
        self.storage_runner = None

    def init_app(self):
        storage_factory = self.get_storage_factory("minio")
        self.storage_runner = storage_factory()

    def save(self, filename, data):
        try:
            self.storage_runner.save(filename, data)
        except Exception as e:
            logger.exception("Failed to save file: %s", e)
            raise e

    def load(self, filename: str, /, *, stream: bool = False) -> Union[bytes, Generator]:
        try:
            if stream:
                return self.load_stream(filename)
            else:
                return self.load_once(filename)
        except Exception as e:
            logger.exception("Failed to load file: %s", e)
            raise e

    def load_once(self, filename: str) -> bytes:
        try:
            return self.storage_runner.load_once(filename)
        except Exception as e:
            logger.exception("Failed to load_once file: %s", e)
            raise e

    def load_stream(self, filename: str) -> Generator:
        try:
            return self.storage_runner.load_stream(filename)
        except Exception as e:
            logger.exception("Failed to load_stream file: %s", e)
            raise e

    def download(self, filename, target_filepath):
        try:
            self.storage_runner.download(filename, target_filepath)
        except Exception as e:
            logger.exception("Failed to download file: %s", e)
            raise e

    @staticmethod
    def get_storage_factory(storage_type: str) -> type[BaseStorage]:
        match storage_type:
            case StorageType.MINIO:
                from domain.rag.storage.impl.minio import MinioStorage
                return MinioStorage


storage = Storage()


def init_app():
    storage.init_app()
