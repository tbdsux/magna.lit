import os
import sys

sys.path.append(os.getcwd())


from sources.manganato import Manganato  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=Manganato,
    search_query="doctor",
    manhwa_slug="manga-kp987798",
    chapter_url="https://chapmanganato.com/manga-kp987798/chapter-115",
)


if __name__ == "__main__":
    test.run()
