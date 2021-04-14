from Xtranews.models import NewsArticle , SportsNewsArticle , TechNewsArticle , HealthNewsArticle , ScienceNewsArticle , BusinessNewsArticle , EntertainmentNewsArticle
import feedparser
from Xtranews import mrEncoder
from bs4 import BeautifulSoup
import lxml
import requests as rs
from dateutil import parser


ZNews_Categories = {
    'India':'https://zeenews.india.com/rss/india-national-news.xml',
    'Business':'https://zeenews.india.com/rss/business.xml',
    'Sports':'https://zeenews.india.com/rss/sports-news.xml',
    'Entertainment':'https://zeenews.india.com/rss/entertainment-news.xml',
    'Tech':'http://zeenews.india.com/rss/technology-news.xml',
    'Health':'https://zeenews.india.com/rss/health-news.xml',
    'Science':'	https://zeenews.india.com/rss/science-environment-news.xml',
}

def ZeeNews():
    #Zeenews
    feed = feedparser.parse(ZNews_Categories["India"])
    for item in feed.entries:
        article = NewsArticle()
        if not NewsArticle.objects.filter(link=item.link).exists():
         if not NewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists():  
          if not NewsArticle.objects.filter(title = item.title).exists():   
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()

    #ZeeNews Sports
    feed = feedparser.parse(ZNews_Categories["Sports"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
         if not SportsNewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists():
          if not SportsNewsArticle.objects.filter(title = item.title).exists():     
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()

    #ZeeNews Tech
    feed = feedparser.parse(ZNews_Categories["Tech"])
    for item in feed.entries:
        article = TechNewsArticle()
        if not TechNewsArticle.objects.filter(link=item.link).exists():
         if not TechNewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists():   
          if not TechNewsArticle.objects.filter(title = item.title).exists():     
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()

    #ZeeNews Health
    feed = feedparser.parse(ZNews_Categories["Health"])
    for item in feed.entries:
        article = HealthNewsArticle()
        if not HealthNewsArticle.objects.filter(link=item.link).exists():
         if not HealthNewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists(): 
          if not HealthNewsArticle.objects.filter(title = item.title).exists():        
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()

    # Business
    feed = feedparser.parse(ZNews_Categories["Business"])
    for item in feed.entries:
        article = BusinessNewsArticle()
        if not BusinessNewsArticle.objects.filter(link=item.link).exists():
         if not BusinessNewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists():      
          if not BusinessNewsArticle.objects.filter(title = item.title).exists():  
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()

    # Entertainment
    feed = feedparser.parse(ZNews_Categories["Entertainment"])
    for item in feed.entries:
        article = EntertainmentNewsArticle()
        if not EntertainmentNewsArticle.objects.filter(link=item.link).exists():
         if not EntertainmentNewsArticle.objects.filter(shortedUrl = mrEncoder.encodeTitle(item.title)).exists():      
          if not EntertainmentNewsArticle.objects.filter(title = item.title).exists():      
            r = rs.get(item.link , headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(r.content , "html5lib")
            tag_image = soup.find("meta" , attrs={'property':'og:image'})
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['content']
            article.description = item.description
            article.publisher = 'Zee News'
            article.link = item.link
            article.save()