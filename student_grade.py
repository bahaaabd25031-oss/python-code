class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade.capitalize()
        
    def introduce(self):
        if self.passed() in ['passed','failed']:
            print(f'my name is {self.name} and my grade is "{self.grade}" ')
        else:
            print('error. you didn\'t enter a valid grade. ')
        
    def passed(self):
        if self.grade in ['A','B','C','D']:
            return 'passed'
        elif self.grade == 'F':
            return 'failed'
        else:
            return 'error'
        
n = int(input('the number of students is: '))

all_students = []

for _ in range(n):
    name = input('enter the name of the student: ')
    grade = input('enter the grade: ')
    s = student(name,grade)
    all_students.append(s)
    
for s in all_students:
    s.introduce()
    print(s.passed())