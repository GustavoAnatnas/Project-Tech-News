import pip._vendor.requests as requests
import time
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
    urls = sel.css('a.cs-overlay-link::attr(href)').getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
