def getBMI (w, h):
    return w / (h/100)**2

print("Your height in cm:")
h = float(input())
print("-"*30)

print("Your weight in kg:")
w = float(input())
BMI = getBMI(w, h)
print("-"*30)

print(f"Your BMI is:", round(BMI,1))
print("-"*30)

if BMI <= 18.4:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are healthy.")
elif 25 <= BMI <= 29.9:
    print("You are over weight.")
elif 30 <= BMI <= 34.9:
    print("You are obese class 1.")
elif 35 <= BMI <= 39.9:
    print("You are obese class 2.")
else:
    print("You are severely obese.")
    
