import scrapy as sp
import pandas as pd
from ..items import DataScrapingNewspageItem

class Scraping_data(sp.Spider):
    df=pd.read_excel(r"C:\Users\Lenovo\Desktop\Python program\data_scraping_newspage\fatf_news.xls")
    start_urls=[df['link'][0]]            
    name='newsspider2'
    count=0                                                  #dates have been scrapped till 187th link,start from 188
    size=len(df['link'])
    def parse(self,response):
        Scraping_data.count=Scraping_data.count+1
        item=DataScrapingNewspageItem()
        date=response.css('div.timestamp  ::attr(title)').extract()
        item['date']=date
        yield item
        nextlink=Scraping_data.df['link'][Scraping_data.count]
        if(Scraping_data.count<Scraping_data.size):
            yield response.follow(nextlink,self.parse)