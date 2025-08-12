<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

# RSS Scraper

A simple Python script (`rss_scraper.py`) that fetches article links from an RSS feed and extracts article text from each link, saving everything to `articles_output.txt`.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

## Quick setup — TL;DR

```bash
# create venv
python3 -m venv venv

# activate (Linux/macOS)
source venv/bin/activate

# or (Windows cmd)
venv\Scripts\activate

# install deps
pip install -r requirements.txt

# run
python rss_scraper.py
```

## What this does

* Reads RSS feed URLs from the `RSS_URL` variable in `rss_scraper.py`.
* Uses `feedparser` to parse the feed and collect article links.
* Uses `requests` + `beautifulsoup4` to fetch each article and extract paragraph text.
* Writes title, link and extracted content to `articles_output.txt`.

## Files

* `rss_scraper.py` — main script (you already have this).
* `requirements.txt` — dependencies:

  ```
  feedparser
  requests
  beautifulsoup4
  ```
* `articles_output.txt` — generated output (created when you run the script).

## Requirements

* Python 3.8+ (3.10 or later recommended)
* pip

## Installation & Usage (expanded)

1. Clone or copy the project files into a directory.
2. Create and activate a virtualenv:

   * Linux/macOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Windows (cmd):

     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Edit `rss_scraper.py` and set `RSS_URL` to the feed you want:

   ```py
   RSS_URL = "https://example.com/rss"
   ```
5. Run:

   ```bash
   python rss_scraper.py
   ```
6. Check `articles_output.txt` for all scraped article titles, links, and content.

## Output format

Each article in `articles_output.txt` looks like:

```
Title: <article title>
Link: <article url>
Content:
<extracted article text>

--------------------------------------------------------------------------------
```

![RSS scraper screenshot](https://raw.githubusercontent.com/Volcann/rss-content-scraper/33e8d7cb997214ab03725be0bf662c894a612ec3/Screenshot%20from%202025-08-12%2012-06-18.png)

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

## Tips & notes

* The script extracts content from `div.article__text` first, then falls back to the first `<article>` tag. Many sites use different classes or HTML structures, so extraction may fail for some publishers. If the output says `Could not extract article content.`, inspect the target page and adjust `content_div = soup.find(...)` to a selector that matches that site.
* Be respectful: check `robots.txt` and the site’s terms of service. Don’t spam requests — consider adding delays if you scrape lots of pages.
* If you need more robust extraction (handling paywalls, JS-rendered pages, or better boilerplate removal), consider tools like `newspaper3k`, `readability-lxml`, or a headless browser (Playwright / Selenium).
* Network issues can happen; the script uses a 10s timeout and returns an error message if requests fail.

## Troubleshooting

* `ModuleNotFoundError`: make sure the virtualenv is activated and `pip install -r requirements.txt` completed.
* Slow or blocked requests: try modifying the `User-Agent` header or add small delays between requests.
* Wrong/empty content: inspect the article HTML and update the selector used in `extract_article_text()`.

## Possible improvements (I can implement these if you want)

* Accept RSS URL as a CLI arg or environment variable.
* Add rate-limiting and retry logic.
* Improve extraction selector matching (try multiple selectors per site).
* Save output in JSON or CSV instead of plaintext.
* Parallelize fetching with concurrency (careful with rate limits).

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">
