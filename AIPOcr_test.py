# import requests
from aip import AipOcr # 百度文字识别库 https://console.bce.baidu.com/ai/?_=1547709733452#/ai/ocr/app/list

# image = requests.get('https://static.pandateacher.com/7b5d6d8d9dea5691705d04fef2306b52.png').content
def get_file_content(filePath):
    with open(filePath, 'rb') as file:
        return file.read()

image = get_file_content('code.jpg')
APP_ID = '15438264'
API_KEY = 'Rpl0oPR6NzSVeQ4AuFcaYIFE'
SECRET_KEY = 'IC2Rz183pl7qUbKlGQR5fPg6YVOrkY4D'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])
else:
    print(res)