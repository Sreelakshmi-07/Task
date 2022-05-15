import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json


class Olx_Scrap(scrapy.Spider):
    name = 'olx'
    base_url = 'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }

    def start_requests(self):
        for page in range(1, 28):
            next_page = self.base_url + str(page)
            yield scrapy.Request(url=next_page, headers=self.headers, callback=self.parse)

    def parse(self, response):
        for house in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
            yield {
                'figure': house.xpath("//a[@class='fhlkh']/figure[@class='_2grx4']").get(),
                "price": house.xpath("//div[@class='IKo3_']/span[@class='_89yzn']/text()").get(),
                "ft": house.xpath("//div[@class='IKo3_']/span[@class='_2TVI3']/text()").get(),
                "name": house.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").get(),
                "place": house.xpath("//div[@class='_1KOFM']/span[@class='tjgMj']/text()").get(),
            }


class Olx_Items(CrawlSpider):
    name = "items"
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page=']
    rules = (
        Rule(LinkExtractor(allow='kozhikode_g4058877/for-rent-houses-apartments_c1723',deny='item')),
        Rule(LinkExtractor(allow='item'),callback='parse_item')
    )
    def parse_item(self,response):
        yield {
            'product':response.xpath("//div[@class='rui-2CYS9']/section[@class='_2wMiF']/h1[@class='_3rJ6e']/text()").get()
        }





# def parse_item(self,response):
#     for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']/a[@class='fhlkh']/@href"):
#         yield {
#             'property_name': houses.xpath('//section/h1/text()').extract(),
#             'property_id': houses.xpath('//div/strong/text()').extract(),
#             # 'breadcrumbs': houses.xpath('')
#         }

# //*[@id="container"]/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[1]/a
