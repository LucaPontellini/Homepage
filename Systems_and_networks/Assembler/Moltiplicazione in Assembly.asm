
org 100h

num1 DB 0Ah
num2 DB 01h

risultato DB ?

mov AL,num1
mov BL,num2

mul BL

mov risultato,AL

ret