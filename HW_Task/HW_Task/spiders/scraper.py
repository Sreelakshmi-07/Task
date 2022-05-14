import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

base = 'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page={}'


class OlxScrap(scrapy.Spider):
    name = 'olx'
    start_urls = [base.format(1)]

    def parse(self, response):

        for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
            try:
                yield {
                    'name': response.css('span._2tW1I::text').get(),
                    'price': response.css('span._89yzn::text').get(),
                    'ft': response.css('span._2TVI3::text').get(),
                    'place': response.css('span.tjgMj::text').get(),
                    'link': response.css('a.fhlkh').attrib['href']
                }

                next_page = base.format()
                yield scrapy.Request(next_page)
            except:
                print("error")


class Olx_Scraper(CrawlSpider):
    name = 'olxs'
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page={}']
    link_extract = LinkExtractor(restrict_xpaths='//ul/li')
    rule_extract = Rule(link_extract,
                        callback='parse_item',
                        follow=False)
    rules = (
        rule_extract
    )

    def parse_item(self, response):
        yield {
            'property_name': response.xpath('//section/h1/text()').extract(),
            'property_id': response.xpath('//div/strong/text()').extract(),
            'breadcrumbs':response.xpath('')
        }

# next_page =
# def parse(self, response):
#     for house in response.css('li.EIR5N'):
# def parse(self, response):
#     for houses in response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']"):
#         pass
# response.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']").extract()
# houses.xpath("//div[@class='IKo3_']/span[@class='_2tW1I']/text()").getall()
# house =  response.xpath("//ul[@class='rl3f9 _3mXOU']/li[@class='EIR5N']")
