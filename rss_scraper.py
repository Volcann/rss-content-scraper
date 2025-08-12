import feedparser
import requests
from bs4 import BeautifulSoup

# Change this to your own website's link
RSS_URL = "https://anywebsitethatsupportsrss.com/rss"

def get_rss_articles(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        articles.append({"title": title, "link": link})
    return articles

def extract_article_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/115.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Cointelegraph articles typically have content inside <div class="post-content"> or similar
        # content_div = soup.find('div', class_='post-content')
        # My:
        content_div = soup.find('div', class_='article__text')
        if not content_div:
            # fallback if class name changed
            content_div = soup.find('article')
        if not content_div:
            return "Could not extract article content."

        paragraphs = content_div.find_all('p')
        article_text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        return article_text.strip()

    except Exception as e:
        return f"Failed to retrieve article: {str(e)}"

def save_articles_to_file(articles, filename="articles_output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for article in articles:
            f.write(f"Title: {article['title']}\n")
            f.write(f"Link: {article['link']}\n")
            f.write("Content:\n")
            f.write(article['content'])
            f.write("\n" + "-"*80 + "\n\n")
    print(f"Saved {len(articles)} articles to {filename}")

def main():
    print("Fetching RSS feed...")
    articles_info = get_rss_articles(RSS_URL)

    print(f"Found {len(articles_info)} articles. Extracting content...")

    # Extract article content for each article
    for article in articles_info:
        print(f"Processing: {article['title']}")
        article['content'] = extract_article_text(article['link'])

    save_articles_to_file(articles_info)

if __name__ == "__main__":
    main()
