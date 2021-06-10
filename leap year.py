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

