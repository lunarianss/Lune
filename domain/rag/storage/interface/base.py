from abc import ABC, abstractmethod
from collections.abc import Generator


class BaseStorage(ABC):

    def __int__(self):
        pass

    @abstractmethod
    def save(self, filename, data):
        raise NotImplementedError

    @abstractmethod
    def download(self, filename, target_filepath):
        raise NotImplementedError

    @abstractmethod
    def load_once(self, filename: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def load_stream(self, filename: str) -> Generator:
        raise NotImplementedError
