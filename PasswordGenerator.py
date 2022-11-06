import random

print("Enter the lenght of the password:")
pass_len = int(input())

pass_data = range(33,127)
password = " "

for i in range(pass_len):
    password += chr(random.choice(pass_data))
    
print("Your password:", password)

filename = 'C:\\Users\\kacpe\\OneDrive\\Pulpit\\Password\\PSWG.txt'
file = open(filename, 'w+')
file.write(password)
file.write('\n')
