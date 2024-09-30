
org 100h

vect db 3,1,9,5,8,11,9,3,9,4
ris db ?
lenv dw 10h
 
MOV AX,0000h
MOV BX,0000h
MOV CX,0000h
MOV DX,0000h 
  
mov CX,lenv
lea si,vect
inizio_for:

mov bl,[si]
add al,bl 

inc si                       
                                  
loop inizio_for

mov ris,al

ret