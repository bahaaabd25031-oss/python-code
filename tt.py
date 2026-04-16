class plant:
    def __init__(self ,name ,color ,size):
        self.name = name
        self.color = color
        self.size = size
    
    def spin(self):
        print('spinning')
    def describe(self):
        print(self.size ,self.color,self.name,end='')


class fruit(plant):
    def __init__(self ,name ,color ,size ,Is_ripe):
        super().__init__(name ,color ,size)
        self.Is_ripe = Is_ripe
    def describe(self):
        super().describe()
        print(f' and it is {'ripe' if self.Is_ripe else 'not ripe'}',end=' ')
        super().spin()

class flowers(plant):
    def __init__(self ,name ,color ,size ,Num_of_leaves):
        super().__init__(name ,color ,size)
        self.Num_of_leaves = Num_of_leaves
    def describe(self):
        super().describe()
        print(f' and it has {self.Num_of_leaves} leaves',end=' ')
        super().spin()

f1 = flowers('laylac','white','small', 9)
f2 = flowers('sunflower','yellow','very large','alot of')
fr1 = fruit('apple','red' , 'big',False)
fr2 = fruit('watermelon','green','average size',True)
for i in (f1,f2,fr1,fr2):
    i.describe()
