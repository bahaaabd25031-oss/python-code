s = input("Enter a text: ") 
a = s.split(" ") 
l = 0 
 
for i in a: 
    if len(i) > l: 
        l = len(i) 
 
print("*"*(l+4))      # First line 
 
for i in a: 
    print("* ", i, " "*(l-len(i)), " *", sep="") 
print("*"*(l+4))       # Last line