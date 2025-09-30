def model_linear(): #선형회귀 모델을 생성해주는 함수
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    

    dataset=pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    reg = LinearRegression()
    reg.fit(X, y)
    return reg 

model = model_linear()

def predict(hour):
    pred = model.predict([[hour]])
    print(f'{hour}시간 공부했을때 예상점수: {pred[0]:.2f}')

while True:
    hour = input('공부시간>')
    if hour == '':
        break
    elif  not hour.isnumeric():
        print('숫자로 입력하시오')
    else:
        predict(int(hour))