import scrapy


class OlxScrap(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self, response):
        for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
            pass
# response.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']").extract()
# houses.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").getall()
# house =  response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']")
