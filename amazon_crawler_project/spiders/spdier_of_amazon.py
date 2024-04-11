import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazon.amazon_crawler_project.items import AmazonCrawlerProjectItem


class SpdierOfAmazonSpider(scrapy.Spider):
    def __init__(self, search_param, **kwargs):
        self.start_urls = [f"https://www.amazon.com/s?k={search_param}"]
        super().__init__(**kwargs)

    name = "spdier_of_amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com"]
    """https://www.amazon.com/s?k=lapto12300-20000"""
    # create url returner by given param

    def parse(self, response):

        # create item
        amazon_items = AmazonCrawlerProjectItem()

        # fill the fields
        amazon_items["image_path"] = response.css('.s-image::attr(src)').extract()

        amazon_items["name"] = response.css('.a-size-medium::text').extract()

        amazon_items["detail_url"] = response.css('.a-spacing-none.s-line-clamp-2 a::attr(href)').extract()

        yield amazon_items

        # next page url
        next_page_url = self.start_urls[0]+response.css('.s-pagination-separator::attr(href)').extract_first()

        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)


# Get project settings
project_settings = get_project_settings()

# Specify additional settings for output
output_settings = {
    'FEED_FORMAT': 'json',  # setting the format to JSON
    'FEED_URI': 'output.json'  # setting the output file name
}

# Merge project settings with output settings
settings = dict(project_settings)
settings.update(output_settings)


# run the program
if __name__ == "__main__":
    process = CrawlerProcess(settings)
    process.crawl(SpdierOfAmazonSpider, search_param="laptop")
    process.start()
