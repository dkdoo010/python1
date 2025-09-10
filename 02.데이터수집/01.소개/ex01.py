import requests
import os

path = f'{os.getcwd()}/data'

if not os.path.exists(path):
    os.makedirs(path)

name = input('이름>')

url=f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uq8hqY3b-NkqmHBgKS9xzRFsJd68YxnQqXZ0YI1vLWbx74P-HB5jYNR9ehU8zZhY1pWhcvPw7aR-heDa0orPab1S7FkaxTeoOJQ-bdUK2P2UhelO3VGOsjmFEm5l8pyPoWGZTbyLKn-dLkbmTsgh1e_VL_IAgzzkB9YlnpiGCSOhT1vQpmCZb7SHxLWGfVHNWsmV55x0&q={최민식}&sa=X&sqi=2&ved=2ahUKEwjK8OKK9riPAxU9slYBHUvpFyQQtKgLegQIFBAB&biw=1536&bih=730&dpr=1.25'
res = requests.get(url)

file_name = f'data/{name}.html'
file_name = path + '/google.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)


