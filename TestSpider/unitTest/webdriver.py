# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

#
start_url = r'http://huaban.com/all/'
# driver = webdriver.Chrome()
# driver.get(start_url)
# driver.find_element_by_link_text(u"登录").click()
# driver.find_element_by_name("account").clear()
# driver.find_element_by_name("account").send_keys("")  # 修改为自己的用户名
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("")  # 修改为自己的密码
# SignInURL = u"https://www.zhihu.com/#signin"
# try:
#     if driver.find_element_by_id('captcha'):
#         while True:
#             if not SignInURL == driver.current_url:
#                 break
#             pass
#         pass
# finally:
#     if SignInURL == driver.current_url:
#         driver.find_element_by_css_selector("button.sign-button.submit").click()
#     cookies = driver.get_cookies()
#     driver.close()
#     print cookies

driver2 = webdriver.Chrome()
driver2.get(start_url)
# driver2.find_element_by_link_text(u"登录").click()
# driver2.find_element_by_name("account").clear()
# driver2.find_element_by_name("account").send_keys("xxxxx")  # 修改为自己的用户名
# driver2.find_element_by_name("password").clear()
# driver2.find_element_by_name("password").send_keys("xxxx")  # 修改为自己的密码
# SignInURL = u"http://www.zhihu.com/#signin"
# try:
#     if driver2.find_element_by_id('captcha'):
#         while True:
#             if not SignInURL == driver2.current_url:
#                 break
#             pass
#         pass
# finally:
#     if SignInURL == driver2.current_url:
#         driver2.find_element_by_css_selector("button.sign-button.submit").click()
cookies = driver2.get_cookies()
print cookies
driver = webdriver.Chrome()
driver.get(start_url)
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(start_url)