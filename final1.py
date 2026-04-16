lst = [1,2,3,4,5,6,7]
ctr = 0
for _ in range(5):
    guess = int(input('enter your guess: '))
    if guess in lst:
        ctr += 1
print('the number of correct guesses is: ',ctr)