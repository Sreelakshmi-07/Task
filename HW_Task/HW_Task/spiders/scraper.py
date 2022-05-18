import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class OlxScrap(scrapy.Spider):
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
        for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
            yield {
                'figure': houses.xpath("//a[@class='fhlkh']/figure[@class='_2grx4']").get(),
                "price": houses.xpath("//div[@class='IKo3_']/span[@class='_89yzn']/text()").get(),
                "ft": houses.xpath("//div[@class='IKo3_']/span[@class='_2TVI3']/text()").get(),
                "name": houses.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").get(),
                "place": houses.xpath("//div[@class='_1KOFM']/span[@class='tjgMj']/text()").get(),
            }


class OlxDetails(CrawlSpider):
    name = "items"
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?sorting=desc-relevance',]
    rules = (
        Rule(LinkExtractor(allow='kozhikode_g4058877/for-rent-houses-apartments_c1723', deny="item")),
        Rule(LinkExtractor(allow="item"), callback='parse')
    )

    def parse(self, response):
        list1 = ' '.join(map(str, response.xpath("//section[@class='_2wMiF']/span[@class='_2xKfz']/text()").getall()))
        convert_list = list1.split(" ")
        price_dict = {"amount": convert_list[1], "currency": convert_list[0]}

        yield {
            'property_name': response.xpath(
                "//div[@class='rui-2CYS9']/section[@class='_2wMiF']/h1[@class='_3rJ6e']/text()").get(),
            'property_id': ' '.join(
                map(str, response.xpath("//div[@class='fr4Cy']/strong/text()").re(r"\d+")
                    )),
            'breadcrumbs': response.xpath("//ol[@class='rui-10Yqz']/li/a/text()").getall(),
            'price': price_dict,
            'img': response.xpath("//figure/img[@class='_39P4_']/@src").get(),
            'description': ' '.join(map(str, (
                response.xpath(
                    '//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/h3[2]/span/text()').get(),
                response.xpath(
                    '//*[@id="container"]/main/div/div/div/div[4]/section[1]/div/div/div[2]/p/text()').get()))),
            'seller_name': response.xpath("//div[@class='_3oOe9']/text()").get(),
            'location': response.xpath(
                "//div[@class='_2A3Wa']/span[@class='_2FRXm']/text()").get(),
            'property_type': response.xpath(
                "//div[@class='_3_knn'][1]/div[@class='_2ECXs']/span[@class='_2vNpt']/text()").get(),
            'bathroom': int(response.xpath(
                "//div[@class='_3_knn'][3]/div[@class='_2ECXs']/span[@class='_2vNpt']/text()").get()),
            'bedrooms': int(response.xpath(
                "//div[@class='_3JPEe']/div[@class='_3_knn'][2]/div[@class='_2ECXs']/span[@class='_2vNpt']/text()"
            ).get())
        }
