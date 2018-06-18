import scrapy
from scrapy.spiders import Spider
import re


from scraper_app.items import House


class HouseSpider(Spider):
    name = 'HouseSpider'
    allowed_domains = ['www.finn.no']
    start_urls = ['https://www.finn.no/realestate/homes/search.html?ownership_type=4&ownership_type=3']

    def parse(self, response):
        page_number = 1
        for x in range (1, 380):
            try:
                print("HERE IT FINDS A NEW PAGE: " + str(page_number))
                page_number = page_number + 1
                yield scrapy.Request('https://www.finn.no/realestate/homes/search.html?ownership_type=4&ownership_type=3' + '&page=' + str(x),callback = self.parse_dir_pages)
            except:
                break

    def parse_dir_pages(self, response):
        print("HERE IT IS LOOKING AT A NEW PAGE")
        for sel in response.xpath('//*[@id="page-results"]/div[1]/div/div/div/div[2]/div/a'):
            #print('HERE IT IS LOOKING AT A NEW LISTING')
            #print(sel)
            item = House()
            address_full = sel.xpath('.//div/div/div[3]/div[1]/div/text()').extract()[0]
            size = sel.xpath('.//div/div/div[3]/p/span[1]/text()').extract()[0].replace(' m²', '')
            size = size if len(size) < 5 else 0
            price = sel.xpath('.//div/div/div[3]/p/span[2]/text()').extract()[0]
            debt = sel.xpath('.//div/div/div[3]/div[2]/ul/li[3]/text()').extract()

            address_list = address_full.split(",")
            #print(address_list)
            if len(address_list) > 1:
                if address_list[1][:5] == " leil":
                    #print("LEILIGHET")
                    address_list[0:2] = [''.join(address_list[0:2])]

            address = address_list[0]
            #print(address)
            city = address_list[1].lstrip(' ') if len(address_list) > 1 else ""
            #print(1 in address_list)
            #print(city)
            area = address_list[2].lstrip(' ') if len(address_list) > 2 else ""
            address_listthree = address_list[3] if len(address_list) > 3 else ""
            area = area if area != "Oslo" else address_listthree

            price = re.sub('[^0-9]', '', price)
            price = price if len(price) < 9 and price != '' else 0

            debt = debt[0] if debt else "0"
            debt = re.sub('[^0-9]', '', debt)
            debt = ''.join(debt.split())[:-4]
            debt = int(debt) if len(debt) < 9 and debt != '' else 0

            #print(address)
            #print(city)
            #print(area)
            #print(size)
            #print(price)
            #print(debt)

            item['address'] = address
            item['city'] = city
            item['area'] = area
            item['size'] = size
            item['price'] = price
            item['debt'] = debt

            yield item














