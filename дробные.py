format(0.1, '.17f')
print(format(0.1, '.17f'))

from decimal import Decimal
Decimal(1) / Decimal(3)
print(Decimal(1) / Decimal(3))

Decimal(1) / Decimal(3) * Decimal(3) == Decimal(1) # False

from fractions import Fraction
Fraction(1) / Fraction(3) * Fraction(3) == Fraction(1) # True