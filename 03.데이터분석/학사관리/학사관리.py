import os, pandas as pd
# file_pro = '교수.csv'
os.chdir('C:\\python\\03.데이터분석\\학사관리')
file_pro = 'C:\\python\\03.데이터분석\\학사관리\\교수.csv'
def inputNum(title):
    while True:
        num = input(title)
        if num=='':
            return ''
        elif num.isnumeric():
            return int(num)
        else:
            print('숫자로 입력하세요!')

def pro_list():
    pro = pd.read_csv(file_pro, index_col='교수번호')
    for idx, row in pro.iterrows():
        print(idx, row['교수이름'], row['교수학과'], row['임용일'], end=' ')
        print(f'{row["급여"]:,} {row["교수직급"]}')

def pro_search(code):
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    if code in pro.index:
        pro_row = pro.loc[code]
        print(code, pro_row['교수이름'], pro_row['교수학과'])

        print('담당학생-------------------------')
        filt = stu['지도교수'] == code
        stu_rows = stu[filt]
        for idx, row in stu_rows.iterrows():
            print(idx, row['학생이름'], row['학생학과'])

        print('담당강좌--------------------------')
        filt = cou['담당교수'] == code
        cou_rows = cou[filt]
        for idx, row in cou_rows.iterrows():
            print(idx, row['강좌이름'], row['강의시수'])
    else:
        print('해당 교수가 없습니다.')

def stu_list():   
    stu = pd.read_csv('학생.csv')
    pro = pd.read_csv('교수.csv')
    merge = stu.merge(pro, left_on='지도교수', right_on='교수번호')
    merge = merge.sort_values('학생이름')
    for idx, row in merge.iterrows():
        print(idx +1, row['학생번호'], row['학생이름'], row['학생학과'], row['교수이름'], end=' ')
        print(row['생년월일'], row['학년'])

def stu_search(code):
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    enroll = pd.read_csv('수강.csv', index_col=['학생번호', '강좌번호'])
    enroll.fillna(0, inplace=True)
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    if not code in stu.index:
        print('해당 학번이 없습니다')
        return
    
    stu_row = stu.loc[code]
    advisor = stu_row['지도교수']
    pro_row = pro.loc[advisor]
    print(stu_row['학생이름'], stu_row['학생학과'], pro_row['교수이름'])

    
    print('\n수강과목')
    print('-'*50)
    enroll_rows = enroll.loc[code]
    sum = 0

    for idx, row in enroll_rows.iterrows():
        cou_row = cou.loc[idx]  # idx는 강좌번호
        print(idx, cou_row['강좌이름'], row['신청일'], row['점수'])
        sum += row['점수']

    avg = sum / len(enroll_rows)
    print('평균:', avg)

while True:
    os.system('cls')
    print('-' * 50)
    print('**** 학사관리 ****')
    print('-' * 50)
    print('[1]교수목록')
    print('[2]교수검색')
    print('[3]학생목록')
    print('[4]학생검색')
    print('[5]강좌목록')
    print('[6]강좌검색')
    print('[0]프로그램종료')
    print('-' * 50)
    menu = input('메뉴선택>')
    if menu=='0':
        break
    elif menu=='1':
        pro_list()
        input('아무키나 누르세요!')
    elif menu=='2':
        while True:
            code = inputNum('교수번호>')
            if code=='': break
            pro_search(code)
    elif menu=='3':
        stu_list()
        input('아무키나 누르시오')
    elif menu=='4':
        code = inputNum('학생번호>')
        if code=='': break
        stu_search(code)