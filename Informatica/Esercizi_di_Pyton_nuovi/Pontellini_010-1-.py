#Esercizio: Utilizzo di Magic Methods
#Crea una classe Frazione che rappresenta una frazione matematica. La classe deve avere i seguenti attributi:

#numeratore: il numeratore della frazione
#denominatore: il denominatore della frazione
#Implementa i seguenti magic methods per la classe Frazione:

#__add__ per sommare due frazioni.
#__sub__ per sottrarre due frazioni.
#__mul__ per moltiplicare due frazioni.
#__str__ per restituire una rappresentazione leggibile della frazione.
#Importante:

#Supponi che il denominatore sia sempre lo stesso.
#Esempio di utilizzo della classe:

# Esempio di utilizzo
#f1 = Frazione(3, 4)
#f2 = Frazione(2, 4)

# Addizione
#f3 = f1 + f2
#print(f3)  # Output: Frazione(5, 4)

# Sottrazione
#f4 = f1 - f2
#print(f4)  # Output: Frazione(1, 4)

# Moltiplicazione
#f5 = f1 * f2
#print(f5)  # Output: Frazione(6, 16)

# Rappresentazione
#print(f1)  # Output: Frazione(3, 4)
#Prova a creare un'istanza della classe Frazione e a utilizzare i magic methods per eseguire operazioni aritmetiche e confronti.

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator + other.numerator
        return Fraction(new_numerator, self.denominator)

    def __sub__(self, other):
        new_numerator = self.numerator - other.numerator
        return Fraction(new_numerator, self.denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

# Esempio di utilizzo
f1 = Fraction(3, 4)
f2 = Fraction(2, 4)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Fraction(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Fraction(1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Fraction(6, 16)

# Rappresentazione
print(f1)  # Output: Fraction(3, 4)