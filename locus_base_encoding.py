x = [*map(int, input("Order-based: ").split())] # 배열을 다중 입력 값으로 받음
y = [] # x의 0-n 값에 대한 인덱스 값 저장
z = [] # locus-base 배열을 만들 빈 리스트

a=len(x) # 입력 받은 배열 x의 길이를 구함

# 배열 x의 0-n 값에 대한 인덱스 값을 빈 리스트 y에 저장
for i in range(len(x)):
    a = x.index(i) + 1
    y.append(a)

# 가장 뒤의 인덱스 값은 locus-base로 바꿀 때 인덱스 0의 값이 들어가야함
b=y.index(max(y))
y[b]=0

# 새로 변화된 리스트 y에 따라 locus-base에 의한 리스트를 만듦
for j in y:
    z.append(x[j])

# 출력
print(z)