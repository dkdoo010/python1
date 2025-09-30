from flask import Blueprint, render_template, send_file, request
from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

bp = Blueprint('kmeans', __name__, url_prefix='/kmeans')

# ✅ 반드시 graph()보다 위에 있어야 함
def model_kmeans(K):
    dataset = pd.read_csv('data/KMeansData.csv')
    X = dataset.iloc[:, [0, 1]].values
    scaler = StandardScaler()
    X_trans = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=K, random_state=0)
    kmeans.fit(X_trans)

    X_org = scaler.inverse_transform(X_trans)
    centers_org = scaler.inverse_transform(kmeans.cluster_centers_)
    return kmeans, X_org, X_trans, centers_org

@bp.route('/cluster')
def cluster():
    _, _, X_trans, _ = model_kmeans(1)

    inertia_list = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(X_trans)
        inertia_list.append(kmeans.inertia_)

    plt.figure(figsize=(5, 3))
    plt.plot(range(1, 11), inertia_list, marker='o')
    plt.xticks(range(1, 11))
    plt.yticks([50, 100, 150, 200])
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.xlabel('n_cluster')
    plt.ylabel('inertia')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/graph')
def graph():
    no = int(request.args['no'])
    kmeans, X_org, X_trans, centers_org = model_kmeans(no)
    y_pred = kmeans.fit_predict(X_trans)

    plt.figure(figsize=(5, 3))
    for i in range(no):
        index = np.where(y_pred == i)
        x = X_org[index, 0]
        y = X_org[index, 1]
        plt.scatter(x, y, s=100, ec='black')

        cx = centers_org[i, 0]
        cy = centers_org[i, 1]
        plt.scatter(cx, cy, c='yellow', s=300, ec='black', marker='s')
        plt.text(cx, cy, str(i), ha='center', va='center')

    for idx, x in enumerate(X_org):
        plt.text(x[0], x[1], str(idx), ha='center', va='center', color='white', size=7)

    plt.xlabel('hour')
    plt.ylabel('score')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

@bp.route('/data')
def data():
    no = int(request.args['no'])
    kmeans, X_org, X_trans, centers_org = model_kmeans(no)
    y_pred = kmeans.fit_predict(X_trans)

    df = pd.read_csv('data/K-평균.csv')
    df['그룹'] = y_pred
    df = df[:10]
    table = df.to_html(classes='table table-striped table-hover', index=False)
    data = {'table':table}
    return table

@bp.route('/')
def kmeans():
    df = pd.read_csv('data/K-평균.csv')
    df = df[:10]
    table = df.to_html(classes='', index=False)
    table = df.to_html(classes='table table-striped', index=False)
    return render_template('index.html', pageName='kmeans.html', 
                           title='K-평균', table=table)




