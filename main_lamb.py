# работа с лямбда-функциями
def calk3(a, b):
    return a + b

calk5 = lambda a,b: a + b # данная функция по сути - упрощенное объявление функции kalk3(a, b)

def math2(op,x,y):
    print(op(x,y))

math2(calk3, 5, 45)
math2(calk5, 5, 45)
math2(lambda a,b: a + b, 5, 45) # будет работать точно так же как math2(calk3, 5, 45)