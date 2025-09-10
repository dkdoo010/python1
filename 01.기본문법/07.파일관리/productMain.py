from function import *
from productFile import *

def newCode():
    list = fileRead()
    result = sorted(list, key=lambda p:p.code, reverse=True)
    if len(list)==0:
        return 1
    else:
        p=result[0]
        return p.code+1
while True:
    menuPrint('상품관리')
    menu = input ('메뉴선택')
    if menu=="0":
        print("프로그램을 종료합니다")
        break
    elif menu=='1':
        p = Product()
        p.code = newCode()
        print(f'상품코드 > {p.code}')
        p.code = inputNum("상품코드>")
        p.name = input("상품명>")
        p.price = inputNum("상품가격>")
        fileAppend(p)
        print("등록성공")


    elif menu=='2': #검색
        code = inputNum("검색할 상품코드 입력하세요")
        list = fileRead()
        result = [p for p in list if p.code == code]
        if result:
            result[0].print()
        else:
            print("해당 코드 상품이 없습니다")

    elif menu=='3':
        while True:
            sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
            if sort == '':break
            list = fileRead()
            result = []
            if sort==1:result = sorted(list, key=lambda p:p.code)
            if sort==2:result = sorted(list, key=lambda p:p.name)
            if sort==3:result = sorted(list, key=lambda p:p.price)
            if sort==4:result = sorted(list, key=lambda p:p.price, reverse=True)
            print()
            for p in result:
                p.print()
    elif menu=='4':
        seq = inputNum("삭제번호>")
        list = fileRead()
        result = [p for p in list if p.code==seq]
        if len(result) == 0:
            print("삭제할 번호가 없습니다")
            continue
        person = result[0]
        person.print()
        sel = input("삭제할래(y)>")
        if sel== 'Y' or sel == 'y':
            result = [p for p in list if p.code!=seq]
            fileWrite(result)
            print("삭제성공")

    elif menu=='5':
        seq = inputNum('수정번호')
        if seq == '': continue
        list = fileRead()
        result = [p for p in list if p.code==seq]
        if len(result)==0:
            print('번호가 없습니다')
            continue
        product= result[0]
        name = input(f'이름: {product.name}>')
        if name!= '': product.name=name
        price = input(f'주소:{product.price}>')
        if price!= '': product.price= price
        product.print()
        fileWrite(list)
        print('수정완료')