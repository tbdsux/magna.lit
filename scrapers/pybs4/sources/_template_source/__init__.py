# flake8: noqa (pls remove this in your new source for flake8 checking)

from typing import List
from urllib.parse import quote

from sources.base import BaseSource
from sources.response import BaseResponse
from sources.types import GetChapterProps, GetManhwaProps, SearchDataProps
from sources.utils import request

BASE_URL = "https://en.leviatanscans.com/home"


class TemplateSource(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse[List[SearchDataProps]]:
        # implement your scraping and other functions here

        # sample data results
        results: List[SearchDataProps] = []

        # always return base response
        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse[GetManhwaProps]:
        # implement your scraping and other functions here

        # sample result structure
        manhwa: GetManhwaProps = {}

        # always return base response
        return BaseResponse(error=False, data=manhwa)

    @staticmethod
    def get_chapter(chapter_url: str) -> BaseResponse[GetChapterProps]:
        # implement your scraping and other functions here

        # sample result structure
        chapter: GetChapterProps = {}

        # always return base response
        return BaseResponse(error=False, data=chapter)
