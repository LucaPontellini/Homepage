#Esercizio: 
#Date le seguenti liste:

#list_1 = [45,75,25,68,98,12,21,84,54,62]
#list_2 = [42,78,23,74,95,16,27,88,51,66]
#list_3 = [
#{"name":"Giovanni", "surname":"Di Santo", "age":42}, 
#{"name":"Giuseppe", "surname":"Mancini", "age":75}, 
#{"name":"Laura", "surname":"Accardi", "age":25}, 
#{"name":"Lalla", "surname":"Sallusti", "age":68},
#{"name":"Salvo", "surname":"Olivieri", "age":12},
#]

#1) ordinare la prima in ordine crescente
#2) ordinare la seconda in ordine decrescente 
#3) ordinare la terza per età decrescente
#4) ordinare la terza in base alla lunghezza del cognome

list_1 = [45,75,25,68,98,12,21,84,54,62]
list_2 = [42,78,23,74,95,16,27,88,51,66]
list_3 = [
{"name":"Giovanni", "surname":"Di Santo", "age":42}, 
{"name":"Giuseppe", "surname":"Mancini", "age":75}, 
{"name":"Laura", "surname":"Accardi", "age":25}, 
{"name":"Lalla", "surname":"Sallusti", "age":68},
{"name":"Salvo", "surname":"Olivieri", "age":12},
]

list_1.sort ()
print (list_1)

list_2.sort (reverse=True)
print (list_2)

list_3 = sorted (list_3, key=lambda x: x ['age'], reverse=True)

for item in list_3:
    print (item)

list_3 = sorted (list_3, key=lambda x: len (x ['surname']))

for item in list_3:
    print (item)