#Dati in input n valori, calcolarne la somma. Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.

sum = 0

value_1 = int (input ("how many values do you want to insert? '"))

for x in range (value_1):
    value_2 = int ( input ("Enter a number: '"))

    sum += value_2

print (f"The sum is: {sum}")