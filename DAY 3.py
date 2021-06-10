#leap year program
name = int(input("year : "))

if (name%4==0 and name%100!=0) or (name%400==0):
  print( name, "is a leap year")
else:
  print( name, "not a leap year")

# leap year แต่ไม่ทัน
start = int(input())
end = int(input())

count = 0

for year in range (start, end+1):
  if(year%4==0 and year%100!=0) or (year%400==0)
    print (year)
    count = count + 1 # <- count +1 ไปใส่ใน count
print("total number of leap year = ", count) 

#natural number
sum 1 --> input
x = int(input("to which number? "))
sum = 0
for i in range (1, x+1):
  #sum = sum + i วิธีล่างเร็วกว่า
  sum += i
print (sum)

#sum 1^5 --> input^5
x = int(input("to which number? "))
sum = 0
for i in range (1, x+1):
  #sum = sum + i วิธีล่างเร็วกว่า
  sum += i**5
print (sum)

#factorial
x = int(input("to which number? "))
product = 1
for i in range (1, x+1):
  product *= i
print (product)

#sum 1^n --> input^n
x = int(input("x: "))
n = int(input("n: ))
sum = 0
for i in range (1, x+1)
  # sum = sum + i
  sum += i**n

print (sum)

#loop
n = 0
while n < 10:
  print(n)
