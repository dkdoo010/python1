import os
import pandas as pd
score_name = 'data/학생성적.csv'
score = pd.read_csv(score_name)

def inputNum(title):
    while True:
        num = input(title)
        if num=='':
            return 0
        elif not num.isnumeric():
            print('점수는 숫자로입력하세요.')
        else:
            return int(num)
while True:
    os.system('cls')
    print('-' * 50)
    print('************* 성 적 관 리 **************')
    print('-' * 50)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1': #등록
        idx = len(score)
        no = f'{idx+1}번'
        print(f'지원번호>{no}')
        num1 = inputNum('국어>')
        num2 = inputNum('영어>')
        num3 = inputNum('수학>')
        num4 = inputNum('과학>')
        num5 = inputNum('사회>')
        score.loc[idx]=[no, num1, num2, num3, num4, num5]
        score.to_csv(score_name, index=False)
        input('아무키나 누르세요!')
    elif menu=='2':
        print(score)
        input('아무키나 누르세요!') 
    elif menu=='3':
        input('아무키나 누르세요!')   
    elif menu=='4': #삭제
        idx = input('삭제번호>')
        idx = idx + '번'
        filt = score['지원번호']==idx
        search = score[filt].index
        if len(search)==0:
            print('삭제할 지원자가 없습니다.')
        else:
            print(score[filt])
            sel = input('삭제하실래요(Y)>')
            if sel=='Y' or sel=='y':
                score.drop(index=search, inplace=True)
                score.to_csv(score_name, index=False)
        input('아무키나 누르세요!')
    elif menu=='5':
        input('아무키나 누르세요!')
    else:
        input('0~5번을 누르세요!')        
        input('0~5번을 누르세요')
