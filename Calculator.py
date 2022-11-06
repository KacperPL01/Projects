import math

def Add(a,b):
    return a + b
def Sub(a,b):
    return a - b
def Multi(a,b):
    return a * b
def Div(a,b):
    return a / b
def Pow(a,b):
    return a ** b
def Sqr(a):
    return math.sqrt(a)


menu = '''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square 
----------------------
To interrupt, press 0
'''

while True: 
    
    print(menu)
    letter = input('Select:  ')
       
    if letter == '1':
        print('Type numbers to add:')
        c = float(input())
        d = float(input())
        print(Add(c,d))
        input('Press enter')
        continue

    if letter == '2':
        print('Type numbers to substract:')
        c = float(input())
        d = float(input())
        print(Sub(c,d))
        input('Press enter')
        continue
    
    if letter == '3':
        print('Type numbers to multiplication:')
        c = float(input())
        d = float(input())
        print(Multi(c,d))
        input('Press enter')
        continue
    
    if letter == '4':
        print('Type numbers to divide:')
        c = float(input())
        d = float(input())
        print(Div(c,d))
        input('Press enter')
        continue
    
    if letter == '5':
        print('Type numbers to power:')
        c = float(input())
        d = float(input())
        print(Pow(c,d))
        input('Press enter')
        continue
    
    if letter == '6':
        print('Type number to square:')
        c = float(input())
        print(Sqr(c))
        input('Press enter')
        continue
    
    if letter == '0':
        break
    
input('You have to select digits from the menu, press Enter to return!')
