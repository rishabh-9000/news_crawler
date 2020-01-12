import scrapy


class NewspaperItem(scrapy.Item):
    host = scrapy.Field()
    category = scrapy.Field()
    headline = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
