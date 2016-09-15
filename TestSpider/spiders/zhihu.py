# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver



class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'https://www.zhihu.com/',
    )



    def get_cookies(self):
        driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("xxxxx") #修改为自己的用户名
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("xxxxx") #修改为自己的密码
        SignInURL = u"https://www.zhihu.com/#signin"
        try:
            if driver.find_element_by_id('captcha'):
                while True:
                    if not SignInURL == driver.current_url:
                        break
                    pass
                pass
        finally:
            if SignInURL == driver.current_url:
                driver.find_element_by_css_selector("button.sign-button.submit").click()
            cookies = driver.get_cookies()
            driver.close()
            print cookies
            return cookies

    def after_login(self, response):
        sel = scrapy.Selector(response)
        #print response.body
        for i in range(1,10):
            xml = r'//*[@id="feed-%d"]/div[1]/div[2]/div[2]/h2/a/text()' %(i)
            titile = sel.xpath(xml).extract()
            if len(titile):
                print str(titile[0])

    def parse(self, response):
        return scrapy.Request(url=self.start_urls[0], cookies=self.get_cookies(), callback=self.after_login)

