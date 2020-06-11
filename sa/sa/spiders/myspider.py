import scrapy
from ..items import SaItem  
from scrapy.http import FormRequest
import time


class MySpider(scrapy.Spider):
    # url_to_scrape = 'https://www.amazon.com/Goodthreads-Perfect-V-Neck-T-Shirt-Short-Sleeve/dp/B06XWLRX8W/ref=sr_1_1_sspa?dchild=1&keywords=t-shirt&qid=1585037086&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR005TkVRQTJRSkhSJmVuY3J5cHRlZElkPUEwNDM1Mjc3M1E2OUFGMzhYOTVVJmVuY3J5cHRlZEFkSWQ9QTA2MTg0MDEyQlNCRE5BVEdFS0tOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # print(url_to_scrape)
    # time.sleep(500)
    name = 'AmazonSpider'
    start_urls = [
        # url_to_scrape
    #    'https://www.amazon.com/Goodthreads-Perfect-V-Neck-T-Shirt-Short-Sleeve/dp/B06XWLRX8W/ref=sr_1_1_sspa?dchild=1&keywords=t-shirt&qid=1585037086&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR005TkVRQTJRSkhSJmVuY3J5cHRlZElkPUEwNDM1Mjc3M1E2OUFGMzhYOTVVJmVuY3J5cHRlZEFkSWQ9QTA2MTg0MDEyQlNCRE5BVEdFS0tOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    ]

    def parse(self,response):
        items = SaItem()
        print("------------------------------------------------------------------------------------")

        productName = response.css('#productTitle::text').extract()
        comments_of_product = response.css('.a-expander-partial-collapse-content span').css('::text').extract()
        
        img_of_product = response.css('img#landingImage::attr(src)').extract_first()
        price_of_product = response.css('#priceblock_ourprice::text').extract()

        #Finalized
        item_name = productName[0].strip()
        img = img_of_product
        comments = comments_of_product
        price = price_of_product
        

       
        items['item_name'] = item_name
        items['img']= img.strip()
        items['comments']= comments
        items['price'] = price[0]
        

        # print(data)
        print("------------------------------ITEMS------------------------------------------------------")
        # print(img_of_product)
        # print(item_name,price[0],img,comments)
        print(items)
        yield items
        pass
    
    
