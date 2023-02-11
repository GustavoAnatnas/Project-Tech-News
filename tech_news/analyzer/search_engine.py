from datetime import datetime
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
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_str = date_obj.strftime("%d/%m/%Y")
        query = {"timestamp": {"$regex": date_str}}
        news_results = search_news(query)
        return [(result["title"], result["url"]) for result in news_results]
    except ValueError:
        raise ValueError("Data inválida. Use o formato 'YYYY-MM-DD'")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
