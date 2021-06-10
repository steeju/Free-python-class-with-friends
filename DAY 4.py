#ตรวจสอบจำนวนเฉพาะ
num = int(input())

for j in range (2, num):
  check = 1
  for i in range (2,j):
    if (j%i == 0):
      check = 0
  if (check == 1):
    print (j, "is a prime")
  else:
    print (j, "is not prime")

#หรือ# หลังจากบรรทัด 130 เปลี่ยนเป็น 
      # if (check == 1):
        #print (j, "is a prime number")
        #ก็จะปริ้นท์ออกมาแค่ตัวที่เป็น prime number

# print("") คือการบอกให้คอมพิวเตอร์ขึ้นบรรทัดใหม่

a = int(input("how long should it be? "))

for i in range (a):
  row = 0
  column = 0
  print ("#")
