import scrapy
import re
from datetime import datetime

from ..items import NewspaperItem


class TimesofindiaSpider(scrapy.Spider):
    name = 'timesofindia'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/home/headlines']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    def parse(self, response):
        businessHeadlines = response.xpath(
            '//*[@id="c_headlines_wdt_2"]/div[1]/ul/li')
        for businessHeadline in businessHeadlines:
            item = NewspaperItem()

            item['createdAt'] = datetime.now()
            item['clickCount'] = 0
            item['archived'] = False

            item['host'] = 'timesofindia'
            item['category'] = 'business'
            item['headline'] = businessHeadline.xpath(
                './span[@class="w_tle"]/a/text()').extract_first()
            item['url'] = "https://timesofindia.indiatimes.com" + \
                businessHeadline.xpath(
                    './span[@class="w_tle"]/a/@href').extract_first()
            imageCode = item['url'].rsplit('/', 1)[-1]
            imageCode = imageCode.replace('.cms', '')
            item['image'] = 'https://timesofindia.indiatimes.com/thumb/msid-' + \
                imageCode + ',width-400,resizemode-4/' + imageCode + '.jpg'
            item['date'] = businessHeadline.xpath(
                './span[@class="w_bylinec"]/span[@class="strlastupd"]/@rodate'
            ).extract_first()

            yield item
        
        sportsHeadlines = response.xpath(
            '//*[@id="c_headlines_wdt_1"]/div/div/div')
        for sportsHeadline in sportsHeadlines:
            headlines = sportsHeadline.xpath('./ul/li')
            for headline in headlines:
                item = NewspaperItem()

                item['createdAt'] = datetime.now()
                item['clickCount'] = 0
                item['archived'] = False

                item['host'] = 'timesofindia'
                item['category'] = 'sports'
                item['headline'] = headline.xpath(
                    './span[@class="w_tle"]/a/text()').extract_first()
                item['url'] = "https://timesofindia.indiatimes.com" + \
                    headline.xpath(
                        './span[@class="w_tle"]/a/@href').extract_first()
                imageCode = item['url'].rsplit('/', 1)[-1]
                imageCode = imageCode.replace('.cms', '')
                item['image'] = 'https://timesofindia.indiatimes.com/thumb/msid-' + \
                    imageCode + ',width-400,resizemode-4/' + imageCode + '.jpg'
                item['date'] = businessHeadline.xpath(
                    './span[@class="w_bylinec"]/span[@class="strlastupd"]/@rodate'
                ).extract_first()

                yield item
        
        entertainmentHeadlines = response.xpath(
            '//*[@id="c_headlines_wdt_2"]/div/div/div')
        for entertainmentHeadline in entertainmentHeadlines:
            headlines = entertainmentHeadline.xpath('./ul/li')
            for headline in headlines:
                item = NewspaperItem()

                item['createdAt'] = datetime.now()
                item['clickCount'] = 0
                item['archived'] = False

                item['host'] = 'timesofindia'
                item['category'] = 'entertainment'
                item['headline'] = headline.xpath(
                    './span[@class="w_tle"]/a/text()').extract_first()
                item['url'] = "https://timesofindia.indiatimes.com" + \
                    headline.xpath(
                        './span[@class="w_tle"]/a/@href').extract_first()
                imageCode = item['url'].rsplit('/', 1)[-1]
                imageCode = imageCode.replace('.cms', '')
                item['image'] = 'https://timesofindia.indiatimes.com/thumb/msid-' + \
                    imageCode + ',width-400,resizemode-4/' + imageCode + '.jpg'
                item['date'] = businessHeadline.xpath(
                    './span[@class="w_bylinec"]/span[@class="strlastupd"]/@rodate'
                ).extract_first()

                yield item