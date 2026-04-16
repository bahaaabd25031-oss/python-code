lst_old = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] 
lst_odd = [x for x in lst_old if x % 2 != 0]
lst_even = [x for x in lst_old if x % 2 == 0]
print('old list:', lst_old)
print('new list(odd):',lst_odd)
print('new list(even):',lst_even)