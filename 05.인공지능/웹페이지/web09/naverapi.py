import urllib.request
import urllib.parse
import json
import time
import urllib.error

def getNew(query, start, display):
    # start=1
    # display = 100
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



