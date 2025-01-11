#Dati in input n valori, calcolarne la somma. Si chieda quanti valori si vogliono inserire quando inizia il programma, si inizializzi la variabile di somma a zero prima che inizi il ciclo.

number_1 = 0

number_2 = int (input ("How many numbers do you want to enter? '"))

while (number_1 + number_2) <= number_2:
    print (f"The sum of your numbers is: {number_1 + number_2}")

    if (number_1 + number_2) == number_2:
        break

number_2 += number_1