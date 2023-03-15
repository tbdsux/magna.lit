from typing import List, TypedDict


class SearchDataProps(TypedDict):
    image: str
    title: str
    url: str
    slug: str


class ManhwaChapters(TypedDict):
    title: str
    url: str
    release: str


class GetManhwaProps(TypedDict):
    title: str
    image: str
    authors: List[str]
    genres: List[str]
    summary: str
    chapters: List[ManhwaChapters]
    url: str


class GetChapterProps(TypedDict):
    title: str
    images: List[str]
