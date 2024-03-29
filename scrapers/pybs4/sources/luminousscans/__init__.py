from urllib.parse import quote

from sources.base import BaseSource
from sources.bases.mangareader import MangaReader
from sources.response import BaseResponse

BASE_URL = "https://luminousscans.com"


class LuminousScans(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse:
        return MangaReader.search(BASE_URL, BASE_URL + f"/?s={quote(query)}")

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse:
        return MangaReader.get_manhwa(BASE_URL + f"/{manhwa.strip('/')}")

    @staticmethod
    def get_chapter(chapter_url: str) -> BaseResponse:
        return MangaReader.get_chapter(chapter_url)
