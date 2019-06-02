#-*- coding:utf-8 -*-
import time
import requests
import credential
from bs4 import BeautifulSoup
from selenium import webdriver

binary= './chromedriver'
driver=webdriver.Chrome(binary)

f = open('./data/50.txt', 'a')

driver.get('https://pann.nate.com/talk/c20005')
driver.find_element_by_xpath('//*[@id="GnbWrap"]/div[2]/a').click()
driver.find_element_by_name('ID').send_keys(credential.user_id)
driver.find_element_by_name('PASSWD').send_keys(credential.user_password)
driver.find_element_by_xpath('//*[@id="tab_cont1"]/div/input').click()

def search_pann(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    reply_list = soup.select('.usertxt')
    if len(reply_list) != 0:
        try:
            for j in range(0, len(reply_list)):
                f.write(reply_list[j].text.strip().replace('\n', ' ') + '\n')
                print('comment :', reply_list[j].text.strip())
        except:
            pass

for i in range(2,200):
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    tag_list = soup.select('.subject > a')
    driver.get('https://pann.nate.com/talk/c20005?page=' + str(i))
    
    for idx, a_tag in enumerate(tag_list,1):
        #print(idx, a_tag.text.strip())
        search_pann('https://pann.nate.com' + a_tag['href'])
