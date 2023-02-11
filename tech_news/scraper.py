import pip._vendor.requests as requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        return None

    if response.status_code == 200:
        time.sleep(1)
        return response.text
    else:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(html_content)
    urls = sel.css("a.cs-overlay-link::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    next_page_link = sel.css("a.next.page-numbers::attr(href)").get()
    return next_page_link if next_page_link else None


# Requisito 4
def scrape_news(html_content):
    sel = Selector(html_content)

    return {
        "url": sel.css("link[rel=canonical]::attr(href)").get(),
        "title": sel.css("h1.entry-title::text").get().strip(),
        "timestamp": sel.css("li.meta-date::text").get().strip(),
        "writer": sel.css("span.author a::text").get().strip(),
        "reading_time": int(
            sel.css("li.meta-reading-time::text").get().strip().split()[0]
        ),
        "summary": sel.xpath("string(//p[1])").get().strip(),
        "category": sel.css("div.meta-category span.label::text")
        .get()
        .strip(),
    }


# Requisito 5
def get_tech_news(amount):
    news_links = []
    link_page = "https://blog.betrybe.com/"
    while len(news_links) < amount:
        page = fetch(link_page)
        news_links += scrape_updates(page)
        link_page = scrape_next_page_link(page)

    news_list = [scrape_news(fetch(link)) for link in news_links[:amount]]
    create_news(news_list)
    return news_list
