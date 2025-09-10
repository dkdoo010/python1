#집합(set) 튜플과 리스트로도 바꿔서 쓸수도 있음
java = {'유재석', '홍길동', '심청이'}
print(java, type(java))

python = {'심청이','강호동','이순신'}
print(2, python, type(python))

print(3, java.intersection(python)) #인터섹션이 교집함임
print(4, java.union(python)) #합집합 유니온
print(5, java.difference(python)) #차집합, 앞에 것을 기준으로 차집합

java.add('강호동') #추가도 됨
print(6, java)
java.remove('유재석') #삭제
print(7, java)

print(8, java, type(java))
java = list(java)
print(9, java, type(java))
java = tuple(java)
print(10, java, type(java))
java = set(java)
print(11, java, type(java))