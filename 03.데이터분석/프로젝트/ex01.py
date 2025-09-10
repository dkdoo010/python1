import pandas as pd 

df = pd.read_csv('data/score.csv')
df.rename(columns={'Unnamed: 0': '지원번호'}, inplace=True)
df.set_index('지원번호', inplace=True)
search = input('이름>')
filt = df['이름'].str.contains(search)
df = df[filt]
if len(df.index)==0:
    print('검색데이터 없습니다')
else:
    print(df)
    