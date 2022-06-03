from bs4 import BeautifulSoup
import requests

# api 呼叫
url = 'http://www.ngchina.com.cn/api/ex/cms/news/list'

# api 呼叫 body => json
# rawData: {"cmsNews":{"categoryId":30,"isWebsite":"Y"},"pageDomain":{"pageNum":1,"pageSize":12}}
# 推測 categoryId 是對應你要撈取的種類
# rawJson 為呼叫完 api 所回傳的文字，此格式為 JSON 字段。
rawJson = requests.post(url, json={"cmsNews":{"categoryId":30,"isWebsite":"Y"},"pageDomain":{"pageNum":1,"pageSize":12}}).text


import json
from PIL import Image
from io import BytesIO


jsonObj = json.loads(rawJson)
print("資料數: ", jsonObj['total'])

for i in jsonObj['rows']:
    print('標題: ', i['title'],"\n\t| 圖片:", i['pic'])
    
    response = requests.get(i['pic'])
    img = Image.open(BytesIO(response.content))
    display(img)
#     img.show()