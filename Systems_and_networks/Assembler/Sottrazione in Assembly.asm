
org 100h

num1 DB 03h
num2 DB 01h

risultato DB ?

mov AL,num1
mov BL,num2

sub BL,AL

mov risultato,AL

ret