import scrapy
import scrapy_proxy_pool

class ScrapyProject(scrapy.Spider):
    name="fashion"
    start_urls=['https://in.seamsfriendly.com/collections/shorts']
    page=2

    def parse(self, response):
        products=response.css("div.Grid__Cell")
        for p in products:
            title=p.css("h2.ProductItem__Title a::text").extract()
            description=p.css("div.label_icon::text").extract()
            price = p.css("div.ProductItem__PriceList span::text").extract()
            img=p.css("noscript img.ProductItem__Image::attr(src)")[0].extract()
        

            yield {'title':title,
                   'description':description,
                   'price':price,
                   'img':img}

        nextpage='https://in.seamsfriendly.com/collections/shorts?page='+str(self.page)
        if self.page<=3:
            self.page+=1
            yield response.follow(nextpage,callback=self.parse)





