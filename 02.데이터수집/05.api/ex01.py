#도서검색
import requests
import os

def getBooks(url, query, page, size):
    try:
        #"Authorization: KakaoAK ${REST_API_KEY}"
        headers={'Authorization': 'KakaoAK 5cacdaa51d206ff5905771eb113bb8e4'}
        url =f"{url}&query={query}&page={page}&size={size}" 
        res = requests.request(method='get', url=url, headers=headers)
        data = res.json()
        documents = data['documents']
        if len(documents)==0:
            print('검색도서가 없습니다')
        for doc in documents:
            title = doc['title']
            price = doc['sale_price']
            authors = doc['authors']
            publisher=doc['publisher']
            print(title,price,','.join(authors),publisher)
        # print(res)
    except Exception as err:
        print('접속오류', err)


if __name__=='__main__':
    url = "https://dapi.kakao.com/v3/search/book?target=title" 
    page=1
    size=10
    
    os.system('cls')
    while True:
        print()
        query = input('검색도서명>')
        if query=='': break
        getBooks(url, query, page, size)
