lst = [1 ,2 ,3 ,2 ,4 ,1 ,5 ,4 ,6 ,9 ,6]
#unique_values = list(set(lst))
counts = {x: lst.count(x) for x in unique_values}
print("unique values:",unique_values)
print("counts:",counts)