class Matrix:
    def __init__(self, n, m):
        self.__data__=[]
        for i in range(n):
            self.__data__.append([])
            for j in range(m):
                self.__data__[i].append(float("nan"))
    
    def __str__(self):
        s = ""
        for row in self.__data__:
            s = s + "|"
            for item in row:
                s += " " + str(item)
            s = s + " |\n"
        return s

    def printMat(self):
        print (self.__data__)

    def set(self, i, j, v):
        self.__data__[i-1][j-1] = v

    def __add__(self, other):
        m = len(self.__data__)
        n = len(self.__data__[0])
        if m != len(other.__data__) or n != len(other.__data__[0]):
            raise TypeError("Can not add two matrices with different sizes!")
        T = Matrix(m,n)
        for i in range(m):
            for j in range(n):
                T.set(i+1,j+1,self.__data__[i][j]+other.__data__[i][j])
        return T
    
    def transpose(self):
        m =  len(self.__data__[0])
        n = len(self.__data__)
        T = Matrix(m ,n)
        for i in range(m):
            for j in range(n):
                T.set(i+1,j+1,self.__data__[j][i])
        return T

    def __mul__(self, other):
        if type(other) != int and type(other) != float:
            raise TypeError("Multiplication is defined on int and float only!")
        m =  len(self.__data__)
        n = len(self.__data__[0])
        T = Matrix(m,n)
        for i in range(m):
            for j in range(n):
                T.set(i+1, j+1, other*self.__data__[i][j])
        return T




        


m = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i==j:
            m.set(i+1, j+1, 1)
        else:
            m.set(i+1, j+1, 0)

n = Matrix(4,5)
for i in range(4):
    for j in range(5):
        if i==j:
            n.set(i+1, j+1, 1)
        else:
            n.set(i+1, j+1, 0)
               
l = m + n 
p = l.transpose()
q = p * 10
print(m)
print(n)
print(l)
print(p)
print(q)