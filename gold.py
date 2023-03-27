a = int(input("請輸入整數:"))
b = a * 2 + 1

for i in range (1 , b ,2):
	move = round ((b-i)/2)-1
	print (f" "*move ,end = " " )
	print("*"*i)