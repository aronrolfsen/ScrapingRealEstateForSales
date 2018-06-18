from scrapy.item import Item, Field

class House(Item):
    address = Field()
    city = Field()
    area = Field()
    size = Field()
    price = Field()
    debt = Field()
