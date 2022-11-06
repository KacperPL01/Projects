import random

menu = '''
1. Tetrahedron dice
2. Cube dice
3. Octahedron dice
4. Decagon dice
5. Dodecahedron dice
6. Icosahedron dice 
----------------------
To interrupt, press 0
'''

while True: 
    
    print(menu)
    letter = input('Select: ')
    
    if letter == '1': 
        dice = random.randint(1,4)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '2':
        dice = random.randint(1,6)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '3':
        dice = random.randint(1,8)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '4':
        dice = random.randint(1,10)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '5':
        dice = random.randint(1,12)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '6':
        dice = random.randint(1,20)
        print("The value is: ", dice)
        input('Press enter')
        continue
        
    if letter == '0':
        break
