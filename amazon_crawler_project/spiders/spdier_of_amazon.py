import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class SpdierOfAmazonSpider(scrapy.Spider):
    name = "spdier_of_amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    # create url returner by given param
    def start_requests(self, search_param: str):
        """This method parse the given search param and yield it"""
        # parse the param
        search_param = search_param.strip().replace(" ", "+")

        # create url
        url = f"{self.start_urls[0]}/s?k={search_param}"

        # get request
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):



# run the program
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(SpdierOfAmazonSpider)
    process.start()
