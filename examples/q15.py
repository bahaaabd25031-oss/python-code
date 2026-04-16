
import random
c = 0
lst = [random.randint(1,100) for _ in range(10)]
for _ in range(5):
    flag = 0
    n = int(input('guess the number: '))
    for x in lst:
        if x == n: 
            flag = 1
            c +=1
    print('correct!!')if flag else print('incorrect') 
print(lst)
print(c)