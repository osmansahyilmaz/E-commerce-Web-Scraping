import scrapy

# DO NOT FORGET TO CHANGE THIS to FALSE BEFORE RELEASE
debug = True

class PetlebiScrapySpider(scrapy.Spider):
    name = "petlebi_scrapy"
    allowed_domains = ["www.petlebi.com"]
    if debug:
        start_urls = [f'https://www.petlebi.com/alisveris/ara?page={i}'.format(i) for i in range(1,3)]
    else:
        start_urls = [f'https://www.petlebi.com/alisveris/ara?page={i}'.format(i) for i in range(1,220)]

    
    def parse(self, response):
        # Extracting product links using XPath
        
        product_links = response.xpath('//*[contains(@id,"product")]/@href').extract()
        
        for product_link in product_links:
            yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product)


    def parse_product(self, response):

        # Extracting product attributes from each product page
        product = {
            "url": response.url,
            'name': response.xpath('//h1[@class="product-h1"]/text()').get(),
            'price': response.xpath('//div[contains(@class, "pd-price")]//span/text()').get(),
            'category': response.xpath('//ol[@class="breadcrumb"]/li[2]//span[@itemprop="name"]/text()').get(),
            'stock': response.xpath('//select[contains(@class, "pd-basket-select")]/option[last()]/@value').get(),
            'images': response.xpath('//div[contains(@class,"product-detail-main")]/div[contains(@class,"col-sm-5")]/div[contains(@class,"MagicScroll")]//a[@data-zoom-id="photoGallery"]/@href').getall(),
            'brand': response.xpath('//div[@id="hakkinda"]//div[contains(@class, "brand-line")]//span/a/text()').get(),
            'origin': response.xpath('//div[@id="hakkinda"]//div[contains(@class, "pd-d-t") and contains(text(), "MENŞEİ")]/following-sibling::div/span/text()').get(),
            'barkod': response.xpath('//div[@id="hakkinda"]//div[contains(@class, "pd-d-t") and contains(text(), "BARKOD")]/following-sibling::div/text()').get(),
            'skt': response.xpath('//div[@id="hakkinda"]//div[contains(@class, "pd-d-t") and contains(text(), "S.K.T.")]/following-sibling::div/text()').get(),
            'description': response.xpath('//span[@id="productDescription"]//text()').getall(),
        }

        yield product

from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings={
     'FEED_FORMAT': 'json',
     'FEED_URI': 'petlebi_products.json',
     'FEED_EXPORT_ENCODING': 'utf-8',
})
process.crawl(PetlebiScrapySpider)
process.start()