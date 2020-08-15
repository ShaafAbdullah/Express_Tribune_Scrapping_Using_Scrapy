import scrapy as sp
from ..items import DataScrapingNewspageItem
class Scrapping_data(sp.Spider):
    count=20
    name='scrapenews'
    start_urls=['https://tribune.com.pk/pakistan/archives/?page=20']
    def parse(self,response):
        item=DataScrapingNewspageItem()
        all_data=response.css('div.item.span-4 ')
        Scrapping_data.count=Scrapping_data.count+1
        for links in all_data:
            tagline=links.css('a.title::text').extract()
            headline=links.css('p.excerpt::text').extract()
            link=links.css('a.title::attr(href)').extract()
            item['tagline']=tagline
            item['news']=headline
            item['link']=link
            yield item
        nextlink=('https://tribune.com.pk/pakistan/archives/?page='+str(Scrapping_data.count))
        if(Scrapping_data.count<=941):                                        #data of 2019 ends at 941
            yield response.follow(nextlink,self.parse)