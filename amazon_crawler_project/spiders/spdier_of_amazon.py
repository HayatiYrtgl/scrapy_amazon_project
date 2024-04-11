import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazon.amazon_crawler_project.items import AmazonCrawlerProjectItem


class SpdierOfAmazonSpider(scrapy.Spider):

    # override
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open("filtered_url", "r", encoding="utf-8") as url:
            self.start_urls = [url.read()]

    # spider setup
    name = "spdier_of_amazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com"]
    # create url returner by given param

    def parse(self, response):
        all_divs = response.css(".puisg-row").extract()

        for div in all_divs:
            # Convert div string to Selector object
            div_selector = scrapy.Selector(text=div)
            # create item
            amazon_items = AmazonCrawlerProjectItem()

            # querry for name
            if div_selector.css('.a-size-medium::text').extract():
                # fill the fields
                amazon_items["image_path"] = div_selector.css('.s-image::attr(src)').extract()

                amazon_items["name"] = div_selector.css('.a-size-medium::text').extract()

                amazon_items["detail_url"] = div_selector.css('.a-spacing-none.s-line-clamp-2 a::attr(href)').extract()

                amazon_items["price"] = div_selector.css(".a-price-whole::text").extract()

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
    'FEED_URI': 'details.json'  # setting the output file name
}

# Merge project settings with output settings
settings = dict(project_settings)
settings.update(output_settings)


# run the program
if __name__ == "__main__":
    process = CrawlerProcess(settings)
    process.crawl(SpdierOfAmazonSpider)
    process.start()
