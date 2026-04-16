def double_check(lst1,lst2):
    flag = 1
    for i in range(len(lst1)):
        if lst1[i] <= lst2[i]: flag = 0 
    return bool(flag)    
print(double_check([3,3,2],[1,2,1]))