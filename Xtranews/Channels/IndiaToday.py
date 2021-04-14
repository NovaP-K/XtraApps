from Xtranews.models import NewsArticle , SportsNewsArticle , TechNewsArticle , HealthNewsArticle , ScienceNewsArticle 
import feedparser
from Xtranews import mrEncoder
from bs4 import BeautifulSoup
import lxml
import requests as rs
from dateutil import parser

IndiaToday_Categories = {
    'Home':'https://www.indiatoday.in/rss/home',
    'Sports':'https://www.indiatoday.in/rss/1206550',
}

def IndiaToday():
    #IndiaToday
    feed = feedparser.parse(IndiaToday_Categories["Home"])
    for item in feed.entries:
        article = NewsArticle()
        if not NewsArticle.objects.filter(link=item.link).exists():
          if not NewsArticle.objects.filter(title=item.title).exists():   
            soup = BeautifulSoup(item.description , "lxml")
            tag_image = soup.img
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['src']
            soup.a.decompose()
            article.description = soup.find('body').text
            article.publisher = 'India Today'
            article.link = item.link
            article.save()

    #INdiaToday Sports
    feed = feedparser.parse(IndiaToday_Categories["Sports"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
          if not SportsNewsArticle.objects.filter(title=item.title).exists():   
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            soup = BeautifulSoup(item.description , "lxml")
            tag_image = soup.img
            article.title = item.title
            article.pubDate = parser.parse(item.published)
            article.image = tag_image['src']
            soup.a.decompose()
            article.description = soup.find('body').text
            article.publisher = 'India Today'
            article.link = item.link
            article.save()
