from random import randint
x=[*map(int,input("Parent1: ").split())]
y=[*map(int,input("Parent2: ").split())]
num= randint(1,10)
a=[]
b=[]
for i in range(num):
    a.append(x[i])
    b.append(y[i])

for j in range(10-num):
    a.append(y[j])
    b.append(x[j])

print("Cut point: before index %d" %num)
print("Offspring1: ", end='')
for i in range(10):
    print(a[i], end='')
print("\nOffspring2: ", end='')
for i in range(10):
    print(b[i], end='')
