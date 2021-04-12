from Xtranews.models import NewsArticle , SportsNewsArticle , TechNewsArticle , HealthNewsArticle , ScienceNewsArticle , BusinessNewsArticle , EntertainmentNewsArticle
import feedparser
from Xtranews import mrEncoder
from bs4 import BeautifulSoup
import lxml
import requests as rs
from dateutil import parser
import json

TOI_Categories = {
    'India':'http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms',
    'Sports':'http://timesofindia.indiatimes.com/rssfeeds/4719148.cms',
    'Cricket':'http://timesofindia.indiatimes.com/rssfeeds/54829575.cms',
    'Tech':'http://timesofindia.indiatimes.com/rssfeeds/66949542.cms',
    'Health':'http://timesofindia.indiatimes.com/rssfeeds/3908999.cms',
    'Entertainment':'http://timesofindia.indiatimes.com/rssfeeds/1081479906.cms',
    'Business':'http://timesofindia.indiatimes.com/rssfeeds/1898055.cms',
    'Science':'http://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms',
    'Environment':'http://timesofindia.indiatimes.com/rssfeeds/2647163.cms',
}


def TOI():
    #Toi
    feed = feedparser.parse(TOI_Categories["India"])
    for item in feed.entries:
        article = NewsArticle()
        if not NewsArticle.objects.filter(link=item.link).exists():
          if not NewsArticle.objects.filter(title = item.title).exists():  
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
            #print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            print("Hello 5 " + str(item.link))
            article.save()

    #Sports
    feed = feedparser.parse(TOI_Categories["Sports"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()
    
    #Cricket
    feed = feedparser.parse(TOI_Categories["Cricket"])
    for item in feed.entries:
        article = SportsNewsArticle()
        if not SportsNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Tech
    feed = feedparser.parse(TOI_Categories["Tech"])
    for item in feed.entries:
        article = TechNewsArticle()
        if not TechNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Health
    feed = feedparser.parse(TOI_Categories["Health"])
    for item in feed.entries:
        article = HealthNewsArticle()
        if not HealthNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Entertainment
    feed = feedparser.parse(TOI_Categories["Entertainment"])
    for item in feed.entries:
        article = EntertainmentNewsArticle()
        if not EntertainmentNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Business
    feed = feedparser.parse(TOI_Categories["Business"])
    for item in feed.entries:
        article = BusinessNewsArticle()
        if not BusinessNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Science
    feed = feedparser.parse(TOI_Categories["Science"])
    for item in feed.entries:
        article = ScienceNewsArticle()
        if not ScienceNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()

    #Environment
    feed = feedparser.parse(TOI_Categories["Environment"])
    for item in feed.entries:
        article = ScienceNewsArticle()
        if not ScienceNewsArticle.objects.filter(link=item.link).exists():
            soup = BeautifulSoup(item.summary , 'lxml')
            article.shortedUrl = mrEncoder.encodeTitle(item.title)
            article.title = item.title
           # print("Hello 1 " + str(item.title))
            if soup.a:
                article.image = str(soup.a.img['src'])
                #print("Hello 2 " + str(soup.a.img['src']))
            else:
                continue
            soup.a.decompose()
            article.description = str(soup.body.text)
            #print("Hello 3 " + str(soup.body.text))
            article.pubDate = parser.parse(item.published)
            #print("Hello 4 " + str(item.published))
            article.publisher = 'TOI'
            article.link = item.link
            #print("Hello 5 " + str(item.link))
            article.save()