import json
import os
import requests

def getAddress():
    with open('data/hollys.json', 'r', encoding='utf-8') as file:
        address = json.load(file)  
        list = []
        for add in address:
            data={'name':add['name'], 'address':add['address'], 'phone':add['phone'],}
            list.append(data)
        return list

def getXY(query):
    url=f'https://dapi.kakao.com/v2/local/search/address.json?query={query}'
    headers={'Authorization': 'KakaoAK 5cacdaa51d206ff5905771eb113bb8e4'}
    res = requests.request(method='get', url=url, headers=headers)
    data=res.json()
    documents = data['documents']
    x=documents[0]['x']
    y=documents[0]['y']
    return x,y 

# def getAddress2(address):
#     address = address.split(' ')[:4]
#     address = ' '.join(address)
#     print(address)

if __name__=='__main__':
    list=getAddress()
    list_json=[]
    for add in list:
        name = add['name']
        phone = add['phone']
        address = add['address']
        address = address.split(' ')[:4]
        address = ' '.join(address)
        xy = getXY(address)
        x= xy[0]
        y= xy[1]
        print(address, x, y, name, phone)
        data={'name':name, 'address':address, 'phone':phone, 'x':x, 'y':y}
        list_json.append(data)

    with open('data/hollys_location.json', 'w', encoding='utf-8') as file:
        json.dump(list_json, file, indent='\t', ensure_ascii=False)
        
