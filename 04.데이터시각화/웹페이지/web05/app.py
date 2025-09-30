from flask import Flask, render_template, request, send_file
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

plt.rc('font', family='Malgun Gothic')
plt.rc('font', size=10)
plt.rc('axes', unicode_minus=False)

app = Flask(__name__, template_folder='temp')

@app.route('/')
def health():
    return render_template('health.html')

@app.route('/health/graph')
def health_graph():
    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    word = request.args['word']
    filt = df['시도군구'].str.contains(word)
    df = df[filt]
    if len(df) > 0:
        df = df[:10]

    plt.figure(figsize=(8, 6))  # 여기서 그래프 크기 조절 (단위: 인치)
    plt.title('지역별 공공의료기관 수', size=20)
    plt.barh(df['시도군구'], df['count'])

    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')  # bbox_inches='tight'는 여백 제거에 도움
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/health/data')
def health_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'data', '인구수별공공의료기관수.csv')
    page = int(request.args['page'])
    size = int(request.args['size'])
    word = request.args['word']

    df = pd.read_csv(file_path)
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    start = (page - 1) * size
    end = page * size
    df2 = df[start:end]
    count = len(df)
    table = df2.to_html(index=True, classes="table table-dark table-sm-hover")

    data = {'count': count, 'table': table}
    return data

if __name__ == '__main__':
    app.run(port=5000, debug=True)
