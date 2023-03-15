from abc import ABC, abstractmethod
from typing import List

from sources.response import BaseResponse
from sources.types import GetChapterProps, GetManhwaProps, SearchDataProps


class BaseSource(ABC):
    @staticmethod
    @abstractmethod
    def search(query: str) -> BaseResponse[List[SearchDataProps]]:
        pass

    @staticmethod
    @abstractmethod
    def get_chapter(chapter_url: str) -> BaseResponse[GetChapterProps]:
        pass

    @staticmethod
    @abstractmethod
    def get_manhwa(manhwa: str) -> BaseResponse[GetManhwaProps]:
        pass

    # TODO: this could be a future feature
    # @staticmethod
    # @abstractmethod
    # def popular() -> BaseResponse:
    #     pass
