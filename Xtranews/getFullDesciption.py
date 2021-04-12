from django.conf.urls import url
from django.http import HttpResponse
from django.http.response import JsonResponse
from bs4 import BeautifulSoup
from Xtranews import getnews
import requests as rr
from Xtranews import mrEncoder

def getDescription(requests , articleUrl):
    linkToSite = getnews.getSpecificNewsUrl(articleUrl)

    # India Today

    if(linkToSite['fields']['publisher'] == 'India Today'):
        r = rr.get(linkToSite['fields']['link'] , headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find('div', attrs = {'class':'description' , 'itemprop': 'articleBody'})
        if description:
            mrEncoder.replaceLinksFromFullDescription(description , ['a'])
            All_P = description.findAll('p')
            FullStringDescription = ""
            for i in range(len(All_P)):
                FullStringDescription += str(All_P[i])
            return HttpResponse(FullStringDescription)
        else:
            description = soup.find('div', attrs = {'class':'liveBlog-indiatoday'})
            if description:
                mrEncoder.replaceLinksFromFullDescription(description , ['a'])
                All_P = description.findAll('h2' ,attrs = {'class':'short-discription'})
                FullStringDescription = All_P
                return HttpResponse(FullStringDescription)
            else:
                return HttpResponse(linkToSite['fields']['description']) 
                
    # NDTV

    elif(linkToSite['fields']['publisher'] == 'NDTV'):
        r = rr.get(linkToSite['fields']['link'] , headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find('div', attrs = {'class':'story__content'})
        if description:
            mrEncoder.replaceLinksFromFullDescription(description , ['a'])
            for div in description.find_all('div' , attrs={'class':'twitter-tweet'}): 
                div.decompose()
            for section in description.find_all('section'): 
                section.decompose()
        
            for x in description.find_all():
                if x.get_text(strip=True) == 'Promoted':
                    x.extract()
            All_P = description.findAll('p')
            FullStringDescription = ""
            for i in range(len(All_P)):
                FullStringDescription += str(All_P[i])
            return HttpResponse(FullStringDescription)
        else:
            description = soup.find('div', attrs = {'itemprop':'articleBody'})
            if description:
                mrEncoder.replaceLinksFromFullDescription(description , ['a'])
                for div in description.find_all('div' , attrs={'class':' twitter-tweet '}): 
                    div.decompose()
                for script in description.find_all('script'): 
                    script.decompose()

                for section in description.find_all('section'): 
                    section.decompose()
        
                for x in description.find_all():
                    if x.get_text(strip=True) == 'Promoted':
                        x.extract()
                All_P = description.findAll('p')
                FullStringDescription = ""
                for i in range(len(All_P)):
                    FullStringDescription += str(All_P[i])
                return HttpResponse(FullStringDescription)
            else:
                return HttpResponse(linkToSite['fields']['description']) 

    elif(linkToSite['fields']['publisher'] == 'Gadgets360'):
        r = rr.get(linkToSite['fields']['link'] , headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find('div', attrs = {'class':'content_text row description'})
        if description:
            mrEncoder.replaceLinksFromFullDescription(description , ['a'])
            for div in description.find_all('div' , attrs={'class':'twitter-tweet'}): 
                div.decompose()
            for section in description.find_all('section'): 
                section.decompose()
        
            for x in description.find_all():
                if x.get_text(strip=True) == 'Promoted':
                    x.extract()
            All_P = description.findAll('p')
            FullStringDescription = ""
            for i in range(len(All_P)):
                FullStringDescription += str(All_P[i])
            return HttpResponse(FullStringDescription)
        else:
            return HttpResponse(linkToSite['fields']['description']) 

        # Zee News

    if(linkToSite['fields']['publisher'] == 'Zee News'):
        r = rr.get(linkToSite['fields']['link'] , headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find('div', attrs = {'class':'article'})
        if description: 
            mrEncoder.replaceLinksFromFullDescription(description , ['a'])
            for iframe in description.findAll('iframe'):
                iframe.decompose()
            All_P = description.findAll('p')
            FullStringDescription = ""
            for i in range(len(All_P)):
                FullStringDescription += str(All_P[i])
            return HttpResponse(FullStringDescription)
        else:
            description = soup.find('div', attrs = {'class':'liveBlog-indiatoday'})
            if description:
                mrEncoder.replaceLinksFromFullDescription(description , ['a'])
                All_P = description.findAll('h2' ,attrs = {'class':'short-discription'})
                FullStringDescription = All_P
                return HttpResponse(FullStringDescription)
            else:
                return HttpResponse(linkToSite['fields']['description']) 
        
    if(linkToSite['fields']['publisher'] == 'TOI'):
        r = rr.get(linkToSite['fields']['link'] , headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.content, 'html5lib')
        description = soup.find('div', attrs = {'class':'ga-headlines'})
        if description: 
            mrEncoder.replaceLinksFromFullDescription(description , ['a'])
            for div in description.findAll('div'):
                div.decompose()
            FullStringDescription = description
            return HttpResponse(FullStringDescription)
        else:
            description = soup.find('div', attrs = {'class':'Normal'})
            if description:
                mrEncoder.replaceLinksFromFullDescription(description , ['a'])
                for div in description.findAll('div'):
                    div.decompose()
                FullStringDescription = description
                return HttpResponse(FullStringDescription)
            else:
                return HttpResponse(linkToSite['fields']['description']) 
              
