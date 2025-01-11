#Esercizio 4: Metodi Statici

#Obiettivo
#Creare una classe chiamata Calcolatrice che utilizzi metodi statici per eseguire operazioni matematiche di base.
#La classe deve avere metodi statici per l'addizione, la sottrazione, la moltiplicazione e la divisione.

#Istruzioni
#Definisci una classe chiamata Calcolatrice.
#Implementa un metodo statico addizione che prenda due numeri come parametri e restituisca la loro somma.
#Implementa un metodo statico sottrazione che prenda due numeri come parametri e restituisca la loro differenza.
#Implementa un metodo statico moltiplicazione che prenda due numeri come parametri e restituisca il loro prodotto.
#Implementa un metodo statico divisione che prenda due numeri come parametri e restituisca il loro quoziente, assicurandoti di gestire la divisione per zero.

#Esempio di utilizzo
#print(Calcolatrice.addizione(10, 5))       # Output: 15
#print(Calcolatrice.sottrazione(10, 5))     # Output: 5
#print(Calcolatrice.moltiplicazione(10, 5)) # Output: 50
#print(Calcolatrice.divisione(10, 5))       # Output: 2.0

class Calculator:
    @staticmethod
    def addition(number1, number2):
        return number1 + number2
    
    @staticmethod
    def subtraction(number1, number2):
        return number1 - number2
    
    @staticmethod
    def multiplication(number1, number2):
        return number1 * number2
    
    @staticmethod
    def division(number1, number2):
        if number2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return number1 / number2

print(Calculator.addition(10, 5))       # Output: 15
print(Calculator.subtraction(10, 5))    # Output: 5
print(Calculator.multiplication(10, 5)) # Output: 50
print(Calculator.division(10, 5))       # Output: 2.0
try:
    print(Calculator.division(10, 0))   # Should raise ZeroDivisionError
except ZeroDivisionError as e:
    print(e)                            # Output: Division by zero is not allowed