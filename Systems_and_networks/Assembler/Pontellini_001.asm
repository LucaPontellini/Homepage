;Scrivere due programmi in assembly che permettano di fare quanto segue:

;1) Dato un vettore vect1 di 10 elementi inizializzato,                                                
;copiare i valori in un vettore vect2 di 10 elementi non inizializzato. (vect1 DB 3,1,9,5,8,11,9,3,9,4)
 
org  100h

vect1 DB 3,1,9,5,8,11,9,3,9,4
vect2 DB 10 dup (?)

cont DB 10

mov AL,0000h
mov CX,0000h

lea SI,vect1
lea DI,vect2

mov CX, cont

inizio_ciclo:

mov AL, [SI]
mov [DI], AL

inc SI
inc DI

loop inzio_ciclo

ret