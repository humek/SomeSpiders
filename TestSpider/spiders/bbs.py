# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from TestSpider.items import TestspiderItem


class BbsSpider(scrapy.Spider):
    name = "bbsSpider"
    allowed_domains = ["bbs.sjtu.edu.cn"]
    start_urls = (
        'https://bbs.sjtu.edu.cn/bbsall',
    )
    link_extractor = {
        'page': LinkExtractor(allow='bbsdoc,board,\w+\.html$'),
        'page_down': LinkExtractor(allow='bbsdoc,board,\w+,page,\d+\.html$'),
        'content': LinkExtractor(allow='bbscon,board,\w+,file,M\.\d+\.A\.html$'),
    }
    _x_query = {
        'page_content': '//pre/text()[2]',
        'poster': '//pre/a/text()',
        'forum': '//center/text()[2]',
    }

    def parse(self, response):
        for link in self.link_extractor['page'].extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.parse_page)

    def parse_page(self, response):
        for link in self.link_extractor['page_down'].extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.parse_page)

        for link in self.link_extractor['content'].extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.parse_content)

    def parse_content(self, response):
        sel = scrapy.Selector(response)
        items = []
        item = TestspiderItem()
        item['url'] = str(response.url)
        forum = sel.xpath(self._x_query['forum']).extract()
        poster = sel.xpath(self._x_query['poster']).extract()
        page_content = sel.xpath(self._x_query['page_content']).extract()
        item['forum'] = forum
        item['poster'] = poster
        item['content'] = page_content
        items.append(item)
        return items
        # bbsItem_loader = ItemLoader(item=TestspiderItem(), response=response)
        # url = str(response.url)
        # bbsItem_loader.add_value('url', url)
        # bbsItem_loader.add_xpath('forum', self._x_query['forum'])
        # bbsItem_loader.add_xpath('poster', self._x_query['poster'])
        # bbsItem_loader.add_xpath('content', self._x_query['page_content'])
        # return bbsItem_loader.load_item()
