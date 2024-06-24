"""
In Python we can't achieve polimorphism by having two or more methods with the 
same name, as we can with other PLs. 

In the program bellow, only the second function add is valid. In other PLs both
are valid, and the call to the add method would use the one that's got the same
amount of elements listed in parenthesis.

"""

class Calculator:
    def add(self, a, b=0):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # Chamará o segundo add, resultando em um TypeError
print(calc.add(2, 3, 4))   # Chamará o terceiro add, resultando em 9
