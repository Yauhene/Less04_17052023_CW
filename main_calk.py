def calk1(a):
    return a+a

def calk2(a):
    return a*a

def calk3(a, b):
    return a + b

def calk4(a, b):
    return a * b

def math(op,x):
    print(op(x))

def math2(op,x,y):
    print(op(x,y))


math(calk1,5)
math(calk2,5)
math2(calk3, 5, 45)
math2(calk4, 5, 45)
