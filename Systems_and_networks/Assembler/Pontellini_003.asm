;Esercizio 4:
;Dato un vettore di 10 elementi inizializzato a priori così definito: 
;vect DB 3,1,9,5,8,3,3,3,9,4 contare le occorrenze del numero 3 e mettere il risultato nella variabile "ris". 

org  100h

vect1 DB 3,1,9,5,8,11,9,3,9,4
vect2 DB 10 dup (?)

mov CL, 00Ah

lea SI,vect1
lea DI, vect2

inizio_ciclo:

cmp CL,0

je fine_ciclo

dec CL

mov AL,[SI]
mov [DI],AL

inc SI
inc DI

jmp inizio_ciclo

fine_ciclo:

int 20h 