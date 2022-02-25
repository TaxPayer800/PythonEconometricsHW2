import math

def pythagoras(cat_a,cat_b):
 hypo = math.sqrt((cat_a**2)+(cat_b)**2)
 return hypo

def show_hypotenuse():
    a = float(input('Enter cat_a'))
    b = float(input('Enter cat_b'))
    x = pythagoras(a,b)
    print('hypo is', x)
    print('hypo rounded down', math.floor(x))
    print('hypo rounded up', math.ceil(x))
