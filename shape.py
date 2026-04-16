rows = int(input('enter the size of the shape: '))
x = rows
for i in range(rows-1):
    if i == 0: 
        print('*  '*rows)
    else:
        print('*  ' , '   ' * (rows-2) , '*' , sep='')         
print('*  '*rows)            

