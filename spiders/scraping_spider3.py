import scrapy as sp

class Scraping_data(sp.Spider):
    start_urls=['https://dps.psx.com.pk/historical']            
    name='newsspider3'
    def parse(self,response):
        data=response.css('#historicalTable > tbody > tr:nth-child(1) > td:nth-child(1) > strong :: text').extract()
        yield{
            'data':data
        } 
        
        