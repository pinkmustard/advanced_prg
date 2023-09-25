from random import randint
from random import sample
# --------------------------------------------------------
print("- Generated population")

list_a = [] # 10개씩 30개
a=[] # 0-29에서 sample로 중복 없이 4개 뽑기 위해 0 - 29 값 저장하는 리스트
new_list1=[] # 파이널 올라가는 리스트 1개
new_list2=[] # 파이널 올라가는 또다른 1개
winner_list=[] # 우승자 리스트

# --------------------------------------------------------

for j in range(30): # 10개씩 30개 리스트 만들기
    line=[]
    for i in range(10):
        line.append(randint(0,1))
    list_a.append(line)

for i in range(30): # 30개 출력함과 동시에 0-29 값 다 넣는 리스트 a 만들기
    print(i,":", list_a[i], "(f : %d)"%list_a[i].count(1))
    a.append(i)

# --------------------------------------------------------

one_list=sample(a,4) # 0-29인 30개에서 랜덤 4개 추출하기

print("- Tournament selection")
for i in range(4):
    print("parent %d:"%one_list[i], list_a[one_list[i]], "(f : %d)"%list_a[one_list[i]].count(1)) # 뽑은 4개 리스트 출력

# --------------------------------------------------------

random_num1=[] # 확률값 0.0-1.0 값 저장하기 위해서 만듦 (준결승 1경기)
for i in range(10): # 0.0-1.0값 10개를 랜덤하게 넣음 (준결승 1경기)
    random_num1.append(randint(0, 100)/100) 
    
for i in range(10): # 유니폼 크로스오버(준결승 1경기)
    if(random_num1[i]>=0.5):
        new_list1.append(list_a[one_list[0]][i])
    else:
        new_list1.append(list_a[one_list[1]][i])
        
# --------------------------------------------------------

random_num2=[]# 확률값 0.0-1.0 값 저장하기 위해서 만듦 (준결승 2경기)
for i in range(10): # 0.0-1.0값 10개를 랜덤하게 넣음 (준결승 2경기)
    random_num2.append(randint(0, 100)/100)
    
for i in range(10): # 유니폼 크로스오버(준결승 2경기)
    if(random_num1[i]>=0.5):
        new_list2.append(list_a[one_list[2]][i])
    else:
        new_list2.append(list_a[one_list[3]][i])
        
# --------------------------------------------------------

random_num3=[]# 확률값 0.0-1.0 값 저장하기 위해서 만듦 (결승)
for i in range(10):# 0.0-1.0값 10개를 랜덤하게 넣음 (결승)
    random_num3.append(randint(0, 100)/100)
    
for i in range(10):# 유니폼 크로스오버 (결승)
    if(random_num1[i]>=0.5):
        winner_list.append(new_list1[i])
    else:
        winner_list.append(new_list2[i])
        
# --------------------------------------------------------
print("- Uniform crossover") #최종값 출력
print("Offspring:",winner_list, "(f : %d)"%winner_list.count(1)) 