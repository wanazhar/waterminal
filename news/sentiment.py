# news/sentiment.py
from newsapi import NewsApiClient
from textblob import TextBlob
from rich.progress import track

class NewsAnalyzer:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=Config.API_KEYS['newsapi'])
        
    def get_sentiment(self, ticker, days=7):
        articles = self._fetch_articles(ticker, days)
        sentiments = []
        
        for article in track(articles, description="Analyzing articles..."):
            analysis = TextBlob(article['content'])
            sentiments.append({
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity
            })
            
        return self._aggregate_sentiment(sentiments)
        
    def _fetch_articles(self, ticker, days):
        return self.newsapi.get_everything(
            q=ticker,
            language='en',
            sort_by='relevancy',
            from_param=datetime.now() - timedelta(days=days)
        )['articles']
        
    def _aggregate_sentiment(self, sentiments):
        # Calculate average scores and sentiment label
        pass