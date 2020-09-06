import requests 
import lxml.html as html
import os
import datetime


HOME_URL= 'https://www.ktsm.com/local/el-paso-news/'

XPATH_LINK_TO_ARTICLE = '//div[@class="article-list__article-text"]/footer/a[contains(.,"El Paso News")]/../../h3/a/@href'
XPATH_TITLE = '//h1[@class="article-title"]/text()'
XPATH_CONTENT = '//div[@class= "article-content rich-text"]/p/text()'

def parse_home():
    try:
        response=requests.get(HOME_URL)
        if response.status_code==200:
            home=response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(links_to_notices)
            today= datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links_to_notices:
                parse_notice(link,today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()
