from domain.rag.storage.interface.base import BaseStorage
from config.option import minio_storage_config
from minio import Minio
from collections.abc import Generator

import logging

logger = logging.getLogger(__name__)


class MinioStorage(BaseStorage):
    def __init__(self):
        super().__init__()
        self.bucket_name = minio_storage_config.MinioStorageConfig.MINIO_BUCKET_NAME

        self.client = Minio(access_key=minio_storage_config.MinioStorageConfig.MINIO_ACCESS_KEY,
                            secret_key=minio_storage_config.MinioStorageConfig.MINIO_SECRET_KEY, endpoint=minio_storage_config.MinioStorageConfig.MINIO_ENDPOINT, secure=minio_storage_config.MinioStorageConfig.MINIO_USE_SSL)

        if not self.client.bucket_exists(
                self.bucket_name):
            self.client.make_bucket(
                self.bucket_name)

        logger.info("minio is ready!")

    def save(self, filename, data):
        self.client.put_object(self.bucket_name, filename, data)

    def download(self, filename, target_filepath):
        self.client.fget_object(self.bucket_name, filename, target_filepath)

    def load_once(self, filename: str) -> bytes:
        return self.client.get_object(self.bucket_name, filename).read()

    def load_stream(self, filename: str) -> Generator:
        return self.client.get_object(self.bucket_name, filename).stream()
