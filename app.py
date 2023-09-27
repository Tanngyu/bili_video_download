import requests
import re
import json
from pprint import pprint

AV = input ("请输入该视频AV番号(例如 ；BV1v84y1x7Qt )")

url=f'https://www.bilibili.com/video/{AV}/?spm_id_from=333.337.search-card.all.click&vd_source=2392a1a1e9e4da8a25b6084e868e9b60'
headers={'Referer':'https://www.bilibili.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}

a=requests.get(url,headers=headers)
a=a.text

title=input("请输入您要另存为的文件名(尽量不要是中文啦):")
data_goal=re.findall('<script>window.__playinfo__=(.*?)</script>',a)[0]

data_json = json.loads(data_goal)

#pprint(data_json)

audio_url=data_json['data']['dash']['audio'][0]['baseUrl']
video_url=data_json['data']['dash']['video'][0]['baseUrl']

audio=requests.get(audio_url,headers=headers)
audio=audio.content
video=requests.get(video_url,headers=headers)
video=video.content


address = input ("另存为的地址(例如:  D://address//  ):")

with open(address + title +'.mp3',mode='wb') as audio_file:
    audio_file.write(audio)
with open(address+ title+'vidio' +'.mp4',mode='wb') as video_file:
    video_file.write(video)
