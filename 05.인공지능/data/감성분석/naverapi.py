import os
import sys
import urllib.request
import urllib.parse
import json
import time
import urllib.error

def getNew(query, start, display):
    client_id = "DSISkunI4gxjpwj6Yl6J"
    client_secret = "CxLnF9_VmQ"
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}&start={start}&display={display}"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            return result['items']
        else:
            print("Error Code:", rescode)
            return None
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("요청이 너무 많습니다. 잠시 후 재시도합니다.")
            time.sleep(5)
            return None
        else:
            print("HTTP 오류 발생:", e)
            return None
    except Exception as e:
        print("기타 오류 발생:", e)
        return None

if __name__ == '__main__':
    query = '인공지능'
    start = 1
    results = []
    while start <= 100:
        time.sleep(1)  # 요청 간 간격 조절
        news = getNew(query, start, display=100)
        if news is None:
            continue  # 오류 발생 시 다음 루프로 넘어감
        results.extend(news)
        start += 100


    print('데이터 개수:', len(results))
    
    with open('data/감성분석/news.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


