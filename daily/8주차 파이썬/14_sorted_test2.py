from operator import attrgetter
from operator import itemgetter

student_tuples = [
    ('john','A',15),
    ('jane','B',15),
    ('dave','B',10),
]

print(sorted(student_tuples,key=itemgetter(1,2),reverse=True))

s = sorted(student_tuples,key=itemgetter(2),reverse=False)
s = sorted(s,key=itemgetter(1),reverse=True)
print(s)

def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=itemgetter(key),reverse=reverse)
    return xs

r = multisort(list(student_tuples),((1,True),(2,False)))
print(r)

#--------------------------------------------------------------
class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name,self.grade,self.age))

student_object = [
    Student('john','A',15),
    Student('jane','B',15),
    Student('dave','B',10)
]

print(sorted(student_object,key=attrgetter('grade','age'),reverse=True))

s = sorted(student_object,key=attrgetter('age'),reverse=False)
s = sorted(s,key=attrgetter('grade'),reverse=True)
print(s)

def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=attrgetter(key),reverse=reverse)
    return xs

r = multisort(list(student_object),(('grade',True),('age',False)))
print(r)