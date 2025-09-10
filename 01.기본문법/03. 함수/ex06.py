from function import menuPrint, inputnum, grade

scores= [
    {'name':'이순신', 'kor':90, 'eng':80, 'mat':70},
    {'name':'심청이', 'kor':80, 'eng':70, 'mat':60},
]

def search(name):
    isfind = False
    for index, s in enumerate(scores):
        if s['name'].find(name) !=-1:
            isfind = True
            tot = s['kor']+s['eng']+s['mat']
            avg = tot/3
            print(s['name'], s['kor'], s['eng'], s['mat'], f"{avg:.2f}", grade(avg))
    if isfind==False:
        print("검색결과가 없습니다")
    return isfind        
    

while True:
    menuPrint("성적관리")
    menu = input("메뉴선택>")
    if menu=="0":
        print("프로그램을 종료합니다")
        break
    elif menu=="1": #입력
        name = input("이름>")
        kor = inputnum("국어")
        eng = inputnum("영어")
        mat = inputnum("수학")
        scores.append({"name":name, "kor":kor,"eng":eng, "mat":mat})
        print("입력성공")
    elif menu=="3": #목록
         if len(scores)==0:
            print("등록된 데이터가 없습니다!")
            continue
         search('')
    elif menu=="2": #검색
        search_name = input("검색이름>")
        search(search_name)

    elif menu=="4": #삭제
        del_name = input("삭제이름>")
        isfind = search(del_name)
        if isfind == True:
            index = inputnum("삭제번호")
            scores.pop(index)
            print("삭제완료")

    elif menu=="5": #수정
        edit_name = input("수정이름>")
        isfind = search(edit_name)

        if isfind == True:
            index = inputnum("수정번호")
            s = scores[index]
            
            name = input(f"수정이름:{s['name']}>")
            if name != "": s['name'] = name

            kor= inputnum(f"국어:{s['kor']}")
            if kor!=0: s['kor'] =kor 
            
            eng= inputnum(f"영어:{s['eng']}")
            if eng!=0: s['eng'] =eng

            mat= inputnum(f"수학:{s['mat']}")
            if mat!=0: s['mat'] =mat

            scores[index]=s
