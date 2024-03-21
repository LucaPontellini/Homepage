#Esercizio 5: Il governo Meloni ha previsto una rimodulazione degli scaglioni Irpef da 5 a 4. Vorrebbe lo sviluppo di un applicativo che passato in input la RAL di un lavoratore dipendente calcoli la tassazione applicata e il netto in busta paga. Sulla RAL applicare una tassazione previdenziale del 12% in modo da ottenere il reddito imponibile. Sul reddito imponibile applicare i nuovi scaglioni Irpef così definiti dal governo:
# 1. Da 0 fino a 28.000 euro applicare il 23% di tassazione
# 2. Superiori ai 28.000 e fino ai 50.000 euro applicare il 35% sulla parte eccedente
# 3. Per redditi superiori ai 50.000 euro applicare il 43% sulla parte eccedente
# N.B:
# Sulla parte eccedente significa che se il reddito è di 56.000 euro bisogna applicare il 23% su i primi 28.000 euro, il 35% sui 22.000 euro eccedenti fino ai 50.000 e il 43% sui 6.000 euro eccedenti i 50.000 euro.

RAL_employee_1 = int (input ("Enter the RAL of a worker employee: '"))

RAL_employee_2 =  RAL_employee_1 / 12
rest_RAL_employee_2 = RAL_employee_2 % 12

RAL_employee_3 = (RAL_employee_2 % 23) + (rest_RAL_employee_2 % 35)
RAL_employee_4 = rest_RAL_employee_2 % 43

if RAL_employee_2 >= 0 and RAL_employee_2 <= 28000:
    print (f"RAL of a worker employee: {RAL_employee_3:.2f} euro")
elif RAL_employee_2 > 28000 and RAL_employee_2 <= 50000:
    print (f"RAL of a worker employee: {RAL_employee_4:.2f} euro")
else: print ("Error")