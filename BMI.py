# Condition (if-else)

name = (input("what is your name? "))
weight = float(input("weight (kg): "))
height = float(input("height (m): "))

BMI = weight / height ** 2
print ("hello,",name," your BMI is ",BMI)

if BMI < 18.5:
  print("Underweight")
elif BMI < 24.9:
  print("Normal")
elif BMI < 29.9:
  print("Overweight")
else:
  print("Obese")
