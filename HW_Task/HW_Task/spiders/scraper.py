import scrapy


class OlxScrap(scrapy.Spider):
    name = 'olx'
    base_url = 'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }

    def start_requests(self):
        for page in range(0, 28):
            next_page = self.base_url + str(page)
            yield scrapy.Request(url=next_page, headers=self.headers, callback=self.parse)

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

# //*[@id="container"]/main/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[1]/a
