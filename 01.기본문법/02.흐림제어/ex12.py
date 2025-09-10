#1.남탕: 남자이거나 여자이면서 나이가 4세미만
#2.여탕: 여자이거나 남자이면서 나이가 4세미만
while True:
    type = input("1.남탕|2.여탕|0.종료>")
    if type=='0':
        print('프로그램을 종료합니다.')
        break
    elif type=='1' or type=='2':
        gender = input('1.남자|2.여자>')
        if type=='1':
            if gender == '1':
                print('남자이므로 남탕 입장이 가능합니다.')
            else:
                age = int(input('나이>'))
                if age < 4:
                    print('여자지만 4세 미만이므로 남탕 입장이 가능합니다.')
                else:
                    print('여자이고 4세 이상이므로 남탕 입장이 불가합니다.')
                pass
        else:
            if gender == '2':
                print('여자이므로 여탕 입장이 가능합니다.')
            else:
                age = int(input('나이>'))
                if age < 4:
                    print('남자지만 4세 미만이므로 여탕 입장이 가능합니다.')
                else:
                    print('남자이고 4세 이상이므로 여탕 입장이 불가합니다.')
    else:
        print('1,2,0 중에 선택하세요.')