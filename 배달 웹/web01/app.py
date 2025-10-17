from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='temp')
app.secret_key = 'secret-key'

menu_items = [
    {'id': 1, 'name': '빅맥세트', 'price': 5000, 'image': 'images/bigmac.png'},
    {'id': 2, 'name': '상하이세트', 'price': 6000, 'image': 'images/sanghai.png'},
    {'id': 3, 'name': '1955세트', 'price': 7000, 'image': 'images/1955.png'}
]
#로그인
users = {
    'dukyoung': '1234',
    'admin': 'adminpass'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            error = '아이디 또는 비밀번호가 틀렸습니다.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login')) #로그인 안 했으면 로그인 페이지로 이동
    
    if 'cart' not in session:
        session['cart'] = {str(item['id']): {'qty': 0, 'l': 0, 'ice': 0} for item in menu_items}
    return render_template('index.html', menu=menu_items, cart=session['cart'])

@app.route('/update_qty', methods=['POST'])
def update_qty():
    item_id = request.form['item_id']
    qty = int(request.form['qty'])

    if 'cart' not in session:
        session['cart'] = {}

    # 옵션값 포함해서 강제 초기화
    session['cart'][item_id] = {
        'qty': qty,
        'l': session['cart'].get(item_id, {}).get('l', 0),
        'ice': session['cart'].get(item_id, {}).get('ice', 0)
    }

    session.modified = True
    return '', 204

@app.route('/option/<int:item_id>', methods=['GET', 'POST'])
def option(item_id):
    item = next((i for i in menu_items if i['id'] == item_id), None)
    item_id_str = str(item_id)
    base_qty = session['cart'].get(item_id_str, {}).get('qty', 0)

    if base_qty == 0:
        return render_template('option.html', item=item, base_qty=0, selected={'l': 0, 'ice': 0})

    if request.method == 'POST':
        l_qty = min(int(request.form['l_qty']), base_qty)
        ice_qty = max(0, int(request.form['ice_qty']))
        session['cart'][item_id_str]['l'] = l_qty
        session['cart'][item_id_str]['ice'] = ice_qty
        session.modified = True
        return redirect(url_for('index'))

    selected = session['cart'][item_id_str]
    return render_template('option.html', item=item, base_qty=base_qty, selected=selected)

@app.route('/complete')
def complete():
    total = 0
    summary = []

    print("세션 상태:", session['cart'])  # 디버깅용 출력

    for item in menu_items:
        cid = str(item['id'])
        data = session['cart'].get(cid, {})
        qty = data.get('qty', 0)
        l = data.get('l', 0)
        ice = data.get('ice', 0)

        if qty > 0:
            item_total = qty * item['price'] + l * 1000 + ice * 700
            total += item_total
            summary.append(f"{item['name']} {qty}개 (L사이즈 {l}개, 아이스크림 {ice}개)")

    # 주문 완료 후 초기화
    session['cart'] = {str(item['id']): {'qty': 0, 'l': 0, 'ice': 0} for item in menu_items}
    session.modified = True

    return render_template('complete.html', summary=summary, total=total)

if __name__ == '__main__':
    app.run(debug=True)









