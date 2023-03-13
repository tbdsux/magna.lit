import logging

from sources.base import BaseSource

logging.basicConfig(level=logging.DEBUG)


class SourceTester:
    def __init__(
        self, cl: BaseSource, search_query: str, manhwa_slug: str, chapter_url: str
    ) -> None:
        self.cl = cl
        self.search_query = search_query
        self.manhwa_slug = manhwa_slug
        self.chapter_url = chapter_url

    def run(self) -> bool:
        # run .search()
        logging.info("Running SEARCH method of class")
        try:
            r = self.cl.search(self.search_query)
            logging.info(r.json())
        except Exception as e:
            logging.error(str(e))
            return False
        logging.info("Done testing SEARCH method")

        # run .get_manhwa()
        logging.info("Running GET_MAHWA method")
        try:
            r = self.cl.get_manhwa(self.manhwa_slug)
            logging.info(r.json())
        except Exception as e:
            logging.error(str(e))
            return False
        logging.info("Done testing GET_MANHWA method")

        # run .get_chapter()
        logging.info("Running GET_CHAPTER method")
        try:
            r = self.cl.get_chapter(self.chapter_url)
            logging.info(r.json())
        except Exception as e:
            logging.error(str(e))
            return False
        logging.info("Done GET_CHAPTER method")

        return True
