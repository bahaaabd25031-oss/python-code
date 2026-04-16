import random as r
#import needed libraries

def create_password(): # define the function
    password = []
    for ctr in range(7): # the number  of characters in the password
        if ctr == 0: # an uppercase letter
            character = chr(r.randint(65,90))
    
        elif ctr == 1: # an integer
            character = str(r.randint(0,9))
            
        elif ctr == 2: # a special character
            character = r.choice(['%','&','$','@','#'])
            
        else: # ethier a lowercase letter or an uppercase
            if r.randint(0,100) % 2 == 0:
                character = chr(r.randint(97,122))
            else:
                character = chr(r.randint(65,90))

        password.append(character) # append each character
    password = ''.join(password) # turn into string
    print(password)
    return password +'\n'
         
n = int(input('how many passwords to generate: '))

file_name ='passwords.txt' 

f = open(file_name,'w') #create new file
for _ in range(n):
    f.write(create_password())
f.close()