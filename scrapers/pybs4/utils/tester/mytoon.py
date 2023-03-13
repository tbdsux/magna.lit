import os
import sys

sys.path.append(os.getcwd())


from sources.mytoon import MyToon  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=MyToon,
    search_query="mercenary",
    manhwa_slug="mercenary-enrollment",
    chapter_url="https://mytoon.net/mercenary-enrollment-chapter-126",
)

if __name__ == "__main__":
    test.run()
