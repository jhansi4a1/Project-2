from csv import writer
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
driver=webdriver.Firefox()

class flipkart:
    url1="https://www.flipkart.com/search?q=Mobile+is+a+4G%2C+6+GB+RAM+and+128+GB+memory.&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
    url2="https://www.flipkart.com/search?q=Laptop%20is%20i5%2C%208GB%20RAM%20with%201%20TB%20HDD&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    driver.get(url1)
    page1=requests.get(url1)
    soup1=BeautifulSoup(page1.content,"lxml")
    driver.switch_to.new_window('tab')
    driver.get(url2)
    page2=requests.get(url2)
    soup2=BeautifulSoup(page2.content,"lxml")
    def Flipkart_Mobile(self):
        mobile_name=[]
        mobile_price=[]
        for i in range (0,5):
            names = self.soup1.find_all('div',class_="_4rR01T")
            prices=self.soup1.find_all('div',class_="_30jeq3 _1_WHN1")
            mobile_name.append(names[i].get_text())
            mobile_price.append(prices[i].get_text())
        print(mobile_name)
        print(mobile_price)
    def Flipkart_Laptop(self):
        lapnames=[]
        lapprices=[]
        for i in range (0,5):
            laptop_brands=self.soup2.find_all('div',class_="_4rR01T")
            laptop_prices=self.soup2.find_all('div',class_="_30jeq3 _1_WHN1")
            lapnames.append(laptop_brands[i].get_text())
            lapprices.append(laptop_prices[i].get_text())
        print(lapnames)
        print(lapprices)
time.sleep(5)
headers={'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
class amazon:
      url1="https://www.amazon.in/s?k=mobile+is+4G+6+gb+ram+128+gb+memory+card&crid=L0KQ281O32K0&sprefix=mobile+is+4g%2Caps%2C232&ref=nb_sb_noss"
      driver.get(url1)
      page1=requests.get(url1,headers=headers)
      soup1=BeautifulSoup(page1.content,'lxml')
      driver.switch_to.new_window('tab')
      url2="https://www.amazon.in/s?k=laptop+is+i5%2C+8gb+ram+with+1+tb+hdd&crid=2Q28C0S06MVXN&sprefix=%2Caps%2C1887&ref=nb_sb_ss_recent_6_0_recent"
      driver.get(url2)
      page2=requests.get(url2,headers=headers)
      soup2=BeautifulSoup(page2.content,'lxml')
      def Amazon_mobile(self):
              all=[]
              for d in self.soup1.findAll('div', attrs={'class':'a-section a-spacing-small a-spacing-top-small'}):
                names= d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
                print(names)
              for d in self.soup1.findAll('div',attrs={'class':'a-row a-size-base a-color-base'}):
                prices=d.find('span',attrs={'a-price-whole'})
                print(prices)
      def Amazon_laptop(self):
              all2=[]
              for d in self.soup2.findAll('div', attrs={'class':'a-section a-spacing-small a-spacing-top-small'}):
                names= d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
                print(names)
              for d in self.soup2.findAll('div' , attrs={'class':'a-row a-size-base a-color-base'}):
                prices=d.find('span' , attrs={'a-price-whole'})
                print(prices)
a=amazon()
a.Amazon_laptop() 
a.Amazon_mobile()                
        
            
f=flipkart()
f.Flipkart_Mobile()
f.Flipkart_Laptop()

with open('products.csv','w') as f:
  thewriter=writer(f)
  header=['mobile_name','mobileprice','laptopname','lapprice']
  thewriter.writerow(header)

