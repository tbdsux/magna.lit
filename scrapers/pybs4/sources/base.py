from abc import ABC, abstractmethod

from sources.response import BaseResponse


class BaseSource(ABC):
    @staticmethod
    @abstractmethod
    def search(query: str) -> BaseResponse:
        pass

    @staticmethod
    @abstractmethod
    def get_chapter(chapter_url: str) -> BaseResponse:
        pass

    @staticmethod
    @abstractmethod
    def get_manhwa(manhwa: str) -> BaseResponse:
        pass

    @staticmethod
    @abstractmethod
    def popular() -> BaseResponse:
        pass
