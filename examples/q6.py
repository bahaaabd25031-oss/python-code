num = input('enter a number in binary(0 & 1): ')
pos,neg,flag = 0,0,0

for i in range( len(num) - 1):

    if int(num[i]) != 0 and int(num[i]) != 1:
        print('\n it must a binary number(only 1 & 0)')
        break

    if int(num[i+1]) - int(num[i]) == -1:
        neg += 1
        flag = 1
    elif int(num[i+1]) - int(num[i])  == 1:
        pos += 1
        flag = 1

if flag: print('positive change is:',pos,' negative change is: ',neg) 