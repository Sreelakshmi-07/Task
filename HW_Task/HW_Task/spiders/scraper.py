import scrapy


class OlxScrap(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self, response):
        for house in response.css('li.EIR5N'):
            try:
                yield {
                    'name': response.css('span._2tW1I::text').get(),
                    'price': response.css('span._89yzn::text').get(),
                    'ft': response.css('span._2TVI3::text').get(),
                    'place': response.css('span.tjgMj::text').get(),
                    'link': response.css('a.fhlkh').attrib['href']
                }
            except:
                print("error")

    # next_page =

    # def parse(self, response):
#     for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
#         pass
# response.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']").extract()
# houses.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").getall()
# house =  response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']")
