import pip._vendor.requests as requests
import time

# import re
from parsel import Selector


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

    # selector = Selector(html_content)

    # url = selector.css("link[rel=canonical]::attr(href)").get()
    # title = selector.css(".entry-title::text").get().strip()
    # timestamp = selector.css(".meta-date::text").get()
    # writer = selector.css(".author a::text").get()
    # reading_time = selector.css(".meta-reading-time::text").get()
    # summary = selector.xpath("string(//p)").get().strip()
    # category = selector.css(".meta-category span.label::text").get()

    # return {
    #     "url": url,
    #     "title": title,
    #     "timestamp": timestamp,
    #     "writer": writer,
    #     "reading_time": int("".join(re.findall(r"\d", reading_time))),
    #     "summary": summary,
    #     "category": category,
    # }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
