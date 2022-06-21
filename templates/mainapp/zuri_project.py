import random
b=[n for n in range(100)]
random.shuffle(b)
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j] < b[j+1]:
            swapped=True
            tmp=b[j]
            b[j]=b[j+1]
            b[j+1]=tmp
print(b)
