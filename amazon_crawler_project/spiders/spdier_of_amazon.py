import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class SpdierOfAmazonSpider(scrapy.Spider):
    name = "spdier_of_amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    # create url returner by given param
    def start_requests(self):
        """This method contains"""

    def parse(self, response):
        pass


# run the program
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(SpdierOfAmazonSpider)
    process.start()
