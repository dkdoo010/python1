import requests

url='https://ssl.pstatic.net/melona/libs/1542/1542851/aca387c89aa724bee90f_20250901164411440.jpg'
res = requests.get(url)

file_name='data/naver.jpg'
with open(file_name, 'wb') as file:
    file.write(res.content)