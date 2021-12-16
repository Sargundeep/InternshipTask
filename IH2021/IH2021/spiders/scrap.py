import scrapy
from ..items import Ih2021Item
class Scrap(scrapy.Spider):
    name='shooters'
    start_urls = [ 
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
    ]

    def parse(self,response):
        items = Ih2021Item()
        x = response.css('div.product')
        for product in x:
            y= product.css("span.price").extract()
            for i in y:
                price = i.replace('<span class="price"><span class="">','').replace('</span></span>','')
            title = product.css("a.catalog-item-name::text")[0].extract()
            stock = product.css("span.out-of-stock::text")[0].extract()
            maftr = product.css("a.catalog-item-brand::text")[0].extract() 
            items['price']=price
            items['title']=title
            items['stock']=stock
            items['maftr']=maftr
            yield items
