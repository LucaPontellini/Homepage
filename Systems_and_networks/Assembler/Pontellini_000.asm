
org  100h

A db 01h
B db 00h

mov AL,A
mov BL,B

cmp AL,BL

jle ramo_falso

add AL,01h

mov A,AL
    
jmp fine_blocco
    
ramo_falso:

jmp AL,B

add AL,01h

mov B,AL
    
fine_blocco
ret