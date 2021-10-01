#Import modules
from selenium import webdriver
import pandas as pd
import os
from datetime import date
import datetime

#Date
date = date.today()
date_str = str(date)
#date_str = '2021-10-11'
list_date =[]
list_date.append(date_str)

#Datetime
datetime = datetime.datetime.now()
datetime_str = str(datetime)
list_datetime =[]
list_datetime.append(datetime_str)

#Set directory file
path = './chromedriver/' #Location Output

#Web path
A = "https://www.bigc.co.th/sliced-pork-collar-per-kg.html"
web_path = A

#Open webdriver 
driver = webdriver.Chrome(path+"chromedriver.exe")
# ใส่ web path
driver.get(web_path)

#ชื่อสินค้า
hotelnames = driver.find_elements_by_class_name('product-name') 
hotelnames=[name.text for name in hotelnames]
#print(hotelnames)
'''
#รหัสสินค้า
roomnames = driver.find_elements_by_class_name('MasterRoom-headerTitle--text')
roomnames=[name.text for name in roomnames]
print(roomnames)
#print(type(roomnames))
'''
#ราคาสินค้า
pricehotel = driver.find_elements_by_class_name('pricing-product-detail') 
pricehotel=[name.text for name in pricehotel]
#print(pricehotel)

#สร้าง DF ให้เท่ากัน เพราะ ชื่อโรงแรมมี แค่ 1 row
count_1 = len(pricehotel)
hotelnames1=[]
for i in range(count_1):
    hotelnames1.extend(hotelnames)
print(hotelnames1)

stampdate = []
for i in range(count_1):
    stampdate.extend(list_date)
print(stampdate)

#Convert to table (DataFrame) ตั้งชื่อ Columns ว่า MovieNames และ Ratings
DF_Agoda=pd.DataFrame({'Product_name':hotelnames1[0] , 'Price':pricehotel, 'Stampdate': stampdate, 'Createdatetime':list_datetime})

#Export to Excel
DF_Agoda.to_excel(hotelnames[0]+date_str+'.xlsx',index=False)