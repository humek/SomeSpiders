# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from TestSpider.items import TestspiderItem
import lxml


class ZhihuSpider(scrapy.Spider):
    name = "zhihuPost"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'https://www.zhihu.com/',
    )


    def start_requests(self):
        import logging
        selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
        # Only display possible problems
        selenium_logger.setLevel(logging.WARNING)

        driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("xxxxx")  # 修改为自己的用户名
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("xxxxx")  # 修改为自己的密码
        SignInURL = u"https://www.zhihu.com/#signin"
        try:
            html = lxml.html.fromstring(driver.page_source)
            isdisplay = html.xpath(r'//html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[3]/@style')
            print isdisplay
            if 1:
                while True:
                    if not SignInURL == driver.current_url:
                        break
                    pass
                pass
        finally:
            if SignInURL == driver.current_url:
                driver.find_element_by_css_selector("button.sign-button.submit").click()
            self.cookies = driver.get_cookies()
            driver.close()
            print self.cookies
            #count = len(self.cookies)
            cookieJar = {}
            count = 1
            for cookie in self.cookies:
                str = 'cookie%d' %(count)
                cookieJar[str] = cookie
                count += 1
            for url in self.start_urls:
                yield scrapy.Request(url, cookies=self.cookies, meta = cookieJar)


    def parse(self, response):
        sel = scrapy.Selector(response)
        xml_text = r'//*[starts-with(@id,"feed")]/div[1]/div[2]/div[2]/h2/a/text()'
        xml_url = r'//*[starts-with(@id,"feed")]/div[1]/div[2]/div[2]/h2/a/@href'
        titile = sel.xpath(xml_text).extract()
        titleUrl = sel.xpath(xml_url).extract()
        items = []


        for index, key in enumerate(titleUrl):
            item = TestspiderItem()
            if titleUrl[index].find('zhihu') != -1:
                item['url'] = titleUrl[index]
            else:
                item['url'] = self.start_urls[0] + titleUrl[index]
            item['poster'] = titile[index]
            print item
            items.append(item)

        return items