#سكربت يسحب معلومات من موقع معين
import requests
import urllib.request
#مكاتب للوصول للانترنيت
import time
from bs4 import BeautifulSoup
import json
import csv
#مكاتب تمكن من انشاء هذي الصيغ
filecsv = open('SouqDataapple.csv', 'w',encoding='utf8')
#عمل او فتح ملف وخاصية دبليو يعني كتابة واليو تي اف 8 يعني تقبل اللغة العربية
file = open('SouqDataapple.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.amazon.com/s?k=car&i=digital-text&page=5&qid=1587127354&swrs=158C36A4E08191FFA022C0485B475CB8&ref=sr_pg_'
#ملاحضة انو صفحات المواقع بس الرقم بلنهاية يتغير لكن الرابط ثابت فهذا الرابط ثابت
file.write('[\n')
#لازم حصر المعلومات بين اقواس المجموعة فنكتب قوس مجموعة وننزل سطر
data = {}
csv_columns = ['name','price','img']
for page in range(1000):
#لوب بعدد الصفحات الكمراد السحب منها
    print('---', page, '---')
    r = requests.get(url + str(page))
    #متغير يعمل ركوست او وصول للرابط النهائي
    print(url + str(page))
    #طباعة الرباط النهائي لتبيين الصفحة الحالية التي يتم السحب منها
    soup = BeautifulSoup(r.content, "html.parser")
    # متغير قيمته البيوتفل صوب وهية ميثود ثابتة بلبايثون ووضيفتها التحويل 
    # فهنا دنحول من متغير ار الي هوة الرابط النهائي دوت كونتاكت اي المحتوى مالته الى صفحة اج تي ام ال
    ancher=soup.find_all('div',{'class' : 'sg-row'})
    #هذا المتغير قيمته تساوي متغير سوب دوت يوجد كل ديف وكلاس تساوي هيج,هذا راح يصير مصفوفة لان ياخذ عدة عناصر
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('span',{'class':'a-size-medium a-color-base a-text-normal" dir="auto'})
        price = pt.find('span', {'class': 'a-price-whole'})
        img = pt.find('img', {'class': 'a-section aok-relative s-image-fixed-height'})
        priceafterdisc=pt.find('span', {'class': 'a-offscreen'})
        if img:
            writer.writerow({'name': name.text.replace('                    ', '').strip(
                '\r\n'), 'price': itemPrice.text, 'img': img.get('src')})
            data['name'] = name.text.replace(
                '                    ', '').strip('\r\n')
            data['price'] = itemPrice.text
            data['img'] = img.get('src')

            data['SllerAge'] = SllerAge.text
            json_data = json.dumps(data, ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
        print(name.text)
        print(name.price)
        print(name.priceafterdisc)    
file.write("\n]")
filecsv.close()
file.close()