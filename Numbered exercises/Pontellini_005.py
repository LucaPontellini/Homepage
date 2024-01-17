#Esercizio: scrivere un programma che chieda all'utente la sua età e stampi se è un bambino (età 0-12), adolescente (età 13-19), adulto (età 20-64) o anziano (età 65+).

age = int (input ("Enter your age: '"))

if age >= 0 and age <= 12:
    print ("You are a child")
elif age >= 13 and age <= 19:
    print ("You are a teenager")
elif age >= 20 and age <= 64:
    print ("You are adult")
elif age >= 65:
    print ("You are senior")