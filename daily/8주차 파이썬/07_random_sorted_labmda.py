import random

for i in range(20):
    print(random.randint(1,45))

print(random.sample(range(1,46),5))

list1 = ['A','B','C','D','E']

random.shuffle(list1)
print(list1)

print(random.choice(list1))

list2=[5,2,3,1,4]
list2.sort()
print(list2)

# sorted()
print(sorted(list2,reverse=True))
print(list2)

dic = {2:'i',5:'a',7:'o'}
sort_dic = sorted(dic)
print(sort_dic)

def my_key(x):
    return x[1]

print(sorted(dic.items(),key=my_key))

print(sorted(dic.items(),key=lambda x:x[1],reverse=True ))

target = ['  cat ','   tiger ','   dog','snake  ','  aaaaaa']

print(sorted(target))

def my_key1(string):
    return len(string.strip())

print(sorted(target,key=my_key1))

print(sorted(target,key=lambda string:len(string.strip())))

student = [('john','A',15),
            ('jane','B',12),
            ('dave','B',10),
            ('aaa','B',30)
          ]

print(sorted(student,key=lambda x:x[2],reverse=True))

from operator import itemgetter
print('다중정렬',sorted(student,key=itemgetter(1,2),reverse=True))

class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name,self.grade,self.age))

student_class = [
    Student('홍길동','A',20),
    Student('박철수','B',12),
    Student('한정희','B',10)
]   
print(student_class)
print(sorted(student_class,key=lambda x:x.name))

from operator import attrgetter
print('다중정렬',sorted(student_class,key=attrgetter('grade','age')))