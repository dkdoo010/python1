from flask import Flask, render_template, request, send_file
import pandas as pd
import FinanceDataReader as fdr
import matplotlib
matplotlib.use('Agg')  # GUI 백엔드 제거
import matplotlib.pyplot as plt
plt.switch_backend('Agg') 
import os
from io import BytesIO

app = Flask(__name__, template_folder='temp', static_folder='static')

# static 폴더 자동 생성
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='주가예측')

@app.route('/data')
def data():
    code = request.args.get('code')
    start = request.args.get('start')
    end = request.args.get('end')
    page = int(request.args.get('page', 1))
    page_size = 5

    df = fdr.DataReader(code, start, end)
    df = df.sort_index(ascending=True)

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    df_page = df.iloc[start_idx:end_idx]

    return df_page.to_html(classes='table table-striped table-hover')

@app.route('/img1')
def img1():
    code = request.args.get('code', '005930')
    start = request.args.get('start', '2024-01-01')
    end = request.args.get('end', '2025-09-30')

    df = fdr.DataReader(code, start, end)
    if df.empty:
        return "<p>데이터가 없습니다.</p>", 400

    df['year'] = df.index.year
    df['month'] = df.index.month
    group = df.groupby(['year', 'month'])[['Close']].mean().reset_index()

    plt.figure(figsize=(10, 4))
    plt.plot(group.index, group['Close'], marker='o', color="#A82E2E")
    xticks = group.index
    labels = [f'{group.loc[i, "year"]}~{group.loc[i, "month"]}' for i in xticks]
    plt.xticks(xticks, labels, rotation=45)
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')
@app.route('/img2')
def img2():
    code = request.args.get('code', '005930')
    start = request.args.get('start', '2024-01-01')
    end = request.args.get('end', '2025-09-30')

    df = fdr.DataReader(code, start, end)
    if df.empty:
        return "<p>데이터가 없습니다.</p>", 400

    df['year'] = df.index.year
    df['month'] = df.index.month
    group = df.groupby(['year', 'month'])[['Volume']].mean().reset_index()

    plt.figure(figsize=(10, 4))
    plt.bar(group.index, group['Volume'], color="#A82E2E")
    xticks = group.index
    labels = [f'{group.loc[i, "year"]}~{group.loc[i, "month"]}' for i in xticks]
    plt.xticks(xticks, labels, rotation=45)
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(port=5000, debug=True)










