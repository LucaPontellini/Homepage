#Dati in input tre numeri, mostra a video il maggiore.

num1 = int (input ("Enter one number: '"))
num2 = int (input ("Enter one number: '"))
num3 = int (input ("Enter one number: '"))

if num1 > num2 and num1 > num3:
    print ("The first number is greater than the second and the third")
elif num2 > num1 and num2 > num3:
    print ("The second number is greater than the first and the third")
else:
    print ("The third number is greater than the first and the second")