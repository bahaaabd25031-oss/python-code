n = int(input('enter a number: '))
ctr = 0
matrix = [[5, 7, 10], [4, 9, 15], [11, 20, 17]] 
for row in matrix:
    for x in row:
        if x % n == 0: ctr += 1
print(ctr)