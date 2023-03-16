from typing import List
from urllib.parse import quote

from sources.base import BaseSource
from sources.bases.mangareader import MangaReader
from sources.response import BaseResponse
from sources.types import GetChapterProps, GetManhwaProps, SearchDataProps

BASE_URL = "https://flamescans.org"


class FlameScans(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse[List[SearchDataProps]]:
        return MangaReader.search(BASE_URL, BASE_URL + f"/?s={quote(query)}")

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse[GetManhwaProps]:
        return MangaReader.get_manhwa(BASE_URL + f"/{manhwa.strip('/')}")

    @staticmethod
    def get_chapter(chapter_url: str) -> BaseResponse[GetChapterProps]:
        return MangaReader.get_chapter(chapter_url)
