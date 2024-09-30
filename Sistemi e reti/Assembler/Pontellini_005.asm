;Esercizio 5:
;Scrivi un programma assembly che converta un valore decimale (esempio 17) in binario.
;Utilizza un vettore temporaneo dove inserire i resti.
;In un fase successiva, inverti tale vettore in uno definitivo.
;Aggiorna ad ogni divisione la lunghezza logica del vettore.

org  100h

num1 dw 17h
num2 db 02h
vect1 db 20 dup (?)
vect2 db 20 dup (?)
cont dw 0

mov AX,0000h
mov BX,0000h
mov CX,0000h
mov DX,0000h

lea DI,vect1

mov AX,num1
mov BL,num2

inizio_ciclo:

cmp AX,0

je fine_ciclo 

div BL

mov [DI],AH

inc DI

mov AH,0000h

inc cont

jmp inizio_ciclo

fine_ciclo:

dec DI

int 20h