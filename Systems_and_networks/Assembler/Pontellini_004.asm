;Esercizio 4: 
;Dato un vettore di 10 elementi inizializzato a priori così definito:
;vect DB 3,1,9,5,8,3,3,3,9,4 contare le occorrenze del numero 3 e mettere il risultato nella variabile "ris".


org 100h

vect DB 3,1,9,5,8,3,3,3,9,4
ris DB ?
cont DW 10

lea SI,vect

mov CX,cont
mov BL,0000h

inizio_ciclo:

mov AL,[SI]
cmp AL,3
jne fine_if
inc BL

fine_if: 

inc SI
loop inizio_ciclo

mov ris,BL 

int 21h

ret