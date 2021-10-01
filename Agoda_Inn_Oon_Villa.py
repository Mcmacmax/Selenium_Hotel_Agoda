#Import modules
from selenium import webdriver
import pandas as pd
import os
from datetime import date

#สร้าง Stampdate = today
date = date.today()
date_str = str(date)
#date_str = '2021-10-11'
list_date =[]
list_date.append(date_str)

#Set directory file
path = './chromedriver/' #Location Output

#Web path
A = "https://www.agoda.com/th-th/inn-oon-villa/hotel/all/chiang-mai-th.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891472&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn="
B = date_str
C = "&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=THB&isFreeOccSearch=false&tag=db22e9db-2204-0721-cb3a-2acdba0c3274&isCityHaveAsq=false&tspTypes=1&los=1&searchrequestid=0784b483-d07c-41dd-ad04-e7edcb101e14"
web_path = A+B+C

#Open webdriver 
driver = webdriver.Chrome(path+"chromedriver.exe")
# ใส่ web path
driver.get(web_path)

#ชื่อโรงแรม
hotelnames = driver.find_elements_by_class_name('HeaderCerebrum__Name') 
hotelnames=[name.text for name in hotelnames]
#print(hotelnames)

#ชื่อห้องพัก
roomnames = driver.find_elements_by_class_name('MasterRoom-headerTitle--text')
roomnames=[name.text for name in roomnames]
print(roomnames)
#print(type(roomnames))

#ราคาห้องพัก
pricehotel = driver.find_elements_by_class_name('finalPrice') 
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
DF_Agoda=pd.DataFrame({'HotelName':hotelnames1 , 'RoomName':roomnames , 'PriceHotel':pricehotel, 'Stampdate': stampdate})

#Export to Excel
DF_Agoda.to_excel(hotelnames[0]+date_str+'.xlsx',index=False)