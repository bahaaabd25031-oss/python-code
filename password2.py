import random as r 
#import needed libraries

def create_password():  # define the function
    password = []
    for ctr in range(7): # the number  of characters in the password
        if ctr == 0: # an uppercase letter
            character = chr(r.randint(65,90))
        else:
            random = r.choice(['uppercase','lowercase','integer','special'])
            match random:
                case 'uppercase':
                    character = chr(r.randint(65,90))
                case 'lowercase':
                    character = chr(r.randint(97,122))
                case 'integer':
                    character = str(r.randint(0,9))
                case 'special':
                    character = r.choice(['%','&','$','@','#'])
        password.append(character)  # append each character
    password = ''.join(password) # turn into string
    print(password)
    return password +'\n'

n = int(input('how many passwords to generate: '))

file_name ='passwords2.txt'

f = open(file_name,'w')#create new file
for _ in range(n):
    f.write(create_password())
f.close()