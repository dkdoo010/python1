from function import inputnum, grade

kor = inputnum("국어")
eng = inputnum("영어")
mat = inputnum("수학")
avg = (kor+eng+mat)/3
print(f"평균:{avg:.2f} 평점:{grade(avg)}")