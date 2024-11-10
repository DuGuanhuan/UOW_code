import re

import requests
from lxml import etree
def downLoadImage(fileName, downLoadUrl):
    r = requests.get(downLoadUrl)
    fileName = fileName + ".jpg"
    print("正在下载 " + fileName)
    with open("./" + fileName, 'wb') as f:
        f.write(r.content)

response = requests.get("https://car.m.autohome.com.cn/")
response.encoding = 'UTF-8'
html = etree.HTML(response.text)
items = html.xpath('//*[@class="item"]')
for item in items:
    logo_url = item.xpath('./img/@data-src')
    if not logo_url:
        continue
    text = item.xpath('./span')[0].text    
    #downLoadImage(text, logo_url[0])
    import csv

    my_re = re.compile(r'[A-Za-z]', re.S)

    res = re.findall(my_re, text)
    if not len(res):
        print(text)
        with open('a.csv', 'a+', encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([text, text+'.jpg'])

