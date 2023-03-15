# pybs4

A scraper utilizing python mainly.

Uses: `requests`, `bs4`, `lxml`

### Note:

This doesn't work on some sites, please check carefully.

## How to add sources?

Try to clone the dir [`./sources/_template_source`](./sources/_template_source/) and use it as a starter template. Please try to base from the other sources too.

- Create a directory name of the new source

- Extend the base scraper class

  ```python
  # __init__.py

  from sources.base import BaseSource

  class MyNewSource(BaseSource):
      pass
      # implement base functions in here
  ```

  You can use the file as basis [`leviatanscans/__init__.py`](./sources/leviatanscans/__init__.py)

### Registering your new source

- Add the source in the [`__init__.py`](./sources/__init__.py)

  ```python
  # DEFINE NEW SOURCES IN HERE
  SOURCES = {
      "leviatanscans": LeviatanScans,
      "mynewsource": MyNewSource,
    }
  ```

- Check the [`sources.json`](../../web.space/lib/sources.json) in the `web.space` directory

  ```json
  [
    {
      "name": "LeviatanScans",
      "scraper": "pybs4",
      "website": "https://en.leviatanscans.com/home/",
      "source": "leviatanscans",
      "working": true
    },
    // add your new source in here
    {
      "name": "MySource",
      "scraper": "pybs4",
      "website": "https://mynewsource-website.com",
      "source": "mytoon", // please make sure it is similar with the one defined in `./sources/__init__.py`
      "working": true
    }
  ]
  ```

### Testing

The hest way we can test our scraper is with real query / data testing.

- Create your source's tester in `./utils/tester` directory

  This is separated so we can run it independently while debugging our source's scraper.

  ```python
  # mynewsource.py

  import os
  import sys

  sys.path.append(os.getcwd())


  from sources.mynewsource import MySource  # noqa: E402
  from utils import SourceTester  # noqa: E402

  test = SourceTester(
      cl=MySource,
      search_query="manhwa-query",
      manhwa_slug="sample-manhwa-slug",
      chapter_url="https://mynewsource-website.com/chapter-url-sample",
  )


  if __name__ == "__main__":
      test.run()
  ```

- Create a test file in the `tests` directory for `pytest` unit testing.

  ```python
  # test_mynewsource.py

  from utils.tester.mynewsource import test


  def test_mynewsource():
      assert test.run()
  ```

### Check the source if compatible with this scraper

```python
import requests

r = requests.get(website)
assert r.status_code == 200
```

If it doesn't return `200` it won't work.
