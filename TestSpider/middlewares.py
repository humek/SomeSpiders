#-*- coding:utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse

import time


#driver = webdriver.PhantomJS(executable_path='/home/icgoo/pywork/spider/phantomjs',desired_capabilities=dcap)
#driver = webdriver.PhantomJS(executable_path=u'/home/fank/pywork/spider/phantomjs',desired_capabilities=dcap)
#driver = webdriver.PhantomJS()


class SeleniumMiddleware(object):
    def process_request(self, request,spider):
        if request.url.find('robot') == -1:
            driver = webdriver.Chrome()
            driver.get(request.url)
            driver.delete_all_cookies()
            for key, value in request.meta.items():
                if key.find('cookie') != -1:
                    driver.add_cookie(value)
                pass
            pass
            driver.get(request.url)
            element = driver.find_element_by_id('zh-load-more')
            for m in range(1, 10):
                webdriver.ActionChains(driver).move_to_element(element).perform()
                time.sleep(3)
            page = driver.page_source
            driver.close()
            return HtmlResponse(request.url,body = page, encoding = 'utf-8',request = request,)
        else:
            return HtmlResponse(request.url,request = request,)


