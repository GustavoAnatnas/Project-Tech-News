from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    result = []
    title = title.lower()
    news = search_news({"title": {"$regex": f".*{title}.*", "$options": "i"}})
    for new in news:
        result.append((new["title"], new["url"]))
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
