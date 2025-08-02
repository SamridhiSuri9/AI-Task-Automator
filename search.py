from ddgs import DDGS
from newspaper import Article

def search_articles(query, num_results=3):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=num_results):
            url = r.get("href")
            if url:
                try:
                    article = Article(url)
                    article.download()
                    article.parse()
                    results.append(article.text)
                except:
                    continue
    return results
