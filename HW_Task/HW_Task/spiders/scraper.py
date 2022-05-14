import scrapy

base = 'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page={}'


class OlxScrap(scrapy.Spider):
    name = 'olx'
    start_urls = [base.format(1)]

    def parse(self, response):
        for house in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
            # try:
            yield {
                'figure': house.xpath("//a[@class='fhlkh']/figure[@class='_2grx4']").get(),
                "price": house.xpath("//div[@class='IKo3_']/span[@class='_89yzn']/text()").get(),
                "ft": house.xpath("//div[@class='IKo3_']/span[@class='_2TVI3']/text()").get(),
                "name": house.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").get(),
                "place": house.xpath("//div[@class='_1KOFM']/span[@class='tjgMj']/text()").get(),
            }


        # except:
        #     print("error")
# //*[@id="container"]/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[1]/a