import os
import sys

sys.path.append(os.getcwd())


from sources.leviatanscans import LeviatanScans  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=LeviatanScans,
    search_query="legend",
    manhwa_slug="manga/legend-of-the-northern-blade",
    chapter_url="https://en.leviatanscans.com/home/manga/legend-of-the-northern-blade/chapter-147/",
)

if __name__ == "__main__":
    test.run()
