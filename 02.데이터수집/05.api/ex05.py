import requests
import os
def getData(query):  # ← 인자 추가
    url = f'https://dapi.kakao.com/v2/search/image?query={query}&size=20'
    headers = {'Authorization': 'KakaoAK 5cacdaa51d206ff5905771eb113bb8e4'}
    res = requests.get(url, headers=headers)
    data = res.json().get('documents', [])
    return data

if __name__ == '__main__':
    query='추성훈'
    list = getData(query)
    for item in list:
        image_url=item['image_url']
        res= requests.get(image_url)
        
        if res.status_code==200:
            index=image_url.rindex('/')
            file_name=image_url[index+1:]
            #파일 다운로드
            with open(f'data/image/{file_name}', 'wb') as file:
                file.write(res.content)