from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup
from lxml import etree
import time
import pandas as pd




data1 = []
def parsing_data(data):
    soup = BeautifulSoup(data, 'html.parser')
    base = etree.HTML(str(soup))
    table = base.xpath('//table[@class="rgMasterTable CaptionTextInvisible"]/tbody/tr')
    mdata = []
    for i in table:   
      all_data = []
      mun = i.xpath('td[1]/a/text()')[0]
      all_data.append(mun)
      address = i.xpath('td[2]/text()')[0]
      all_data.append(address)
      phone = i.xpath('td[3]/text()')[0]
      all_data.append(phone)
      try:
        all_data.append(i.xpath('td[4]/a/text()')[0])
      except:
        all_data.append('')
      try:
        all_data.append(i.xpath('td[5]/a/text()')[0])
      except:
        all_data.append("")
      mdata.append(all_data)

    return mdata


def str_data(data):
  j = 1
  for i in data:
    if type(i) == list:
      # print(type(i))
      temp = {
        'Municipality':i[0],
        'Address':i[1],
        'Phone no': i[2],
        'Website':i[3],
        'Email':i[4]  
      }
      
      data1.append(temp)
  print(j)
  j += 1
        
    

def main():   
  with sync_playwright() as pw:
    chromium = pw.chromium 
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://alm.imiscloud.com/ALALM/ALALM/About/ALM-Municipal-Directory.aspx")
    time.sleep(5)
    for i in range(23):
      page.locator('//input[@title="Next Page"]').click()
      d = parsing_data(page.content())
      time.sleep(2)
      str_data(d)
    
    t = pd.DataFrame(data1)
    t.to_excel('ALM/alm-data.xlsx')
    
    
if __name__ == "__main__":
    main()