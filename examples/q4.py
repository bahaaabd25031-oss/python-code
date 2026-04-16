n = int(input('enter the number of rows: '))
mat = [[(i +j)**2 for j in range(n)] for i in range(n)]
print(mat)