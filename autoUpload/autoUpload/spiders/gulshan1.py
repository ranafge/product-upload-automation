# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Gulshan1Spider(scrapy.Spider):
    name = 'gulshan1'
    allowed_domains = ['www.gulshan1.com']
    start_urls = ['http://gulshan1.com/wp-admin/post-new.php?post_type=product']
    handle_httpstatus_list = [404,403,302]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def parse(self, response):
        self.driver.get(response.url)

        time.sleep(5)
        self.driver.find_element_by_id("user_login").send_keys("gulshan1")
        self.driver.find_element_by_id("user_pass").send_keys("(uUA3imgpEE%rO(YQ9yiJp1o")
        self.driver.find_elements_by_id('wp-submit')[0].send_keys(Keys.RETURN) # LOGIN SUCCESS
        time.sleep(5)
        df = pd.read_excel('/home/py/Documents/officeWork/autoUpload/autoUpload/Rana.xlsx')
        time.sleep(5)
        df['Item Name']= df['Item Name']+" "+ df['Size']

        for i, r in df.head(n=5).iterrows():
            product_name = r['Item Name']
            selling_price = str(r['Selling Price'])
            catetory = r['Category']
            time.sleep(3)
            #self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(Keys.BACK_SPACE)
            #self.driver.find_element_by_xpath('//*[@id="_regular_price"]').send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            self.driver.find_element(by=By.XPATH,value="//input[@type='text' and @name='post_title']").send_keys(product_name)
            #time.sleep(5)
            #self.driver.find_element_by_xpath('//*[@id="_regular_price"]').clear()
            #self.driver.find_element_by_xpath('//*[@id="_regular_price"]').send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            self.driver.find_element_by_xpath('//input[@type="text" and @class="short wc_input_price"]').send_keys(selling_price)
            time.sleep(10)

            if catetory == "Frozen Food":
                self.driver.find_element_by_xpath('//input[@id="in-product_cat-500" and @value="500"]').click() # frozen fook
            elif catetory == "Cooking Oil":
                self.driver.find_element_by_xpath('//input[@id="in-product_cat-462" and @value="462"]').click() #add new cooking
                self.driver.find_element_by_xpath('//input[@id="in-product_cat-473" and @value="473"]').click() # cooking oil
            elif catetory == "Froot Juice & Instant Drink":
                self.driver.find_element_by_xpath('//input[@id="in-product_cat-251" and @value="251"]').click() #add new drink
                self.driver.find_element_by_xpath('//input[@id="in-product_cat-256" and @value="256"]').click() # juce


            time.sleep(5)
            #self.driver.find_element_by_xpath('//*[@id="save-post"]').send_keys(Keys.ENTER) # draft
            self.driver.find_element_by_xpath('//*[@id="publish"]').send_keys(Keys.ENTER) # publish

            time.sleep(20)
            #self.driver.find_element_by_xpath('//*[@id="title"]').clear()
            #self.driver.find_element_by_xpath('//*[@id="_regular_price"]').clear()
            #time.sleep(3)
            # ele = WebDriverWait.until(EC.element_located_to_be_selected(By.CSS_SELECTOR, "#wpbody-content > div.wrap > a"))
            # ele.send_keys(Keys.ENTER)


            element = WebDriverWait(self.driver, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#wpbody-content > div.wrap > a")) )
            element.send_keys(Keys.ENTER)
        #     self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(product_name)
        #     self.driver.find_element_by_xpath('//*[@id="_regular_price"]').send_keys(selling_price)
        #     self.driver.find_element_by_xpath('//*[@id="save-post"]').send_keys(Keys.ENTER) # draft
            #time.sleep(15)
            #self.driver.find_element_by_xpath('//*[@id="title"]').clear()
            #self.driver.find_element_by_xpath('//*[@id="_regular_price"]').clear()
            #self.driver.find_element_by_xpath('//*[@id="save-post"]').clear()




        # self.driver.find_elements_by_name("post_title")[0].send_keys('product name xxx')
        # self.driver.find_element_by_xpath('//*[@id="title"]').send_keys("product_name")

        self.driver.close()








