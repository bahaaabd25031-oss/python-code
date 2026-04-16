n1 = int(input('entaer the first number:'))
n2 = int(input('entaer the second number:'))

opr = input('enter the operation: ')

match opr:
    case '+':
        print(n1 + n2)
    case '-':
        print(n1-n2)
    case '*':
        print(n1*n2)
    case '/':
        print(n1/n2)
    case '**':
        print(n1**n2)
    case '//':
        print(n1//n2)
    case '%' :
        print(n1%n2)
    case _ :
        print('nigga chose a hard operation hahaha XD')
