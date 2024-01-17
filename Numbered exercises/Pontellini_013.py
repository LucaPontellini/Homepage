#Esercizio: scrivere 10 volte la parola "ciao", sommare i numeri da 10 a 20 (compresi gli estremi), sommare i numeri pari fino a 30 (30 incluso) e moltiplicare i numeri da 1 a 10.

for numbers in range (1,11):
    print ("Hello")

print ("-------------------------------")

sum_1 = 0
for x in range (10,21):
    sum_2 = sum_1 + x 
    print (sum_2)

print ("-------------------------------")

sum_3 = 0
for y in range (2,31,2):
    sum_4 = sum_3 + y
    print (sum_4)

print ("-------------------------------")

multiplication_1 = 1
for z in range (1,11):
    multiplication_2 = multiplication_1 * z
    print (multiplication_2)