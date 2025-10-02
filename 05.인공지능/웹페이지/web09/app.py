from flask import Flask, render_template, request, jsonify
import re
import pandas as pd
from naverapi import getNew
from model import createModel


app = Flask(__name__, template_folder='temp', static_folder='static')

vector, model = createModel()

@app.route('/predict')
def predict():
    text = request.args['text']
    find_text = re.findall(r'[가~힣]+', text)
    join_text = [' '.join(find_text)]
    vector_text = vector.transform(join_text)
    pred = model.predict(vector_text)
    if pred[0] == 1:
        return "긍정."
    else:
        return "부정."



@app.route('/search')
def search():
    query = request.args.get('query', '')
    start = int(request.args.get('start', 1))  # 클라이언트에서 전달된 시작 위치
    display = int(request.args.get('display', 5))  # 클라이언트에서 요청한 개수

    if not query:
        return jsonify([])  # 검색어가 없으면 빈 리스트 반환

    result = getNew(query, start, display)

    return jsonify(result if result else [])






@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='감성분석')

if __name__=='__main__':
    app.run(port=5000, debug=True)












