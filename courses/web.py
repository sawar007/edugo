from bs4 import BeautifulSoup
import requests


def scrap():
    url ='https://www.codewithharry.com/videos/'

    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')

    ele =soup.find_all('div',class_ ='col-md-6')
    res=[]

    for e  in ele:
        key = e.find('h2').text
        desc = e.find('p').get_text().strip()

        link = 'https://www.codewithharry.com/videos/' +e.find('a').get('href')
        res.append({ 'name':key, 'mess':desc , 'l' :link })
    
    return res
    
    





