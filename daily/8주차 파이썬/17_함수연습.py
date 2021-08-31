# def add():
#     return 1,2,3,4,5

# a,b,c,d = add()
# print(a)

# print(end='  ')


# def func(op,*v):
#     print(v)
#     print(type(v))
#     if op == '+':
#         sum = 0
#         for i in v:
#             sum += i
#     return sum

# data = func('+',2,3,4,5,6,7)    
# print(data)


a = 7

def dis():
    global a
    a += 1
    print(a)
    return a


a = dis()
