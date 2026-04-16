lst = [['ali',99],['bahaa',100],['ahmed',89],['hasan',95]]
name = input('enter the name of the student to know the mark: ')
for i in lst:
    if name == i[0]: print(i[0],i[1],sep=':')