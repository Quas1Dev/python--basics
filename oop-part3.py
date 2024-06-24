"""
Neste código, utilizamos o módulo 'abc' (Abstract Base Classes) 
em Python para definir uma classe abstrata chamada Animal. 
Vamos explicar os conceitos envolvidos:

1. abc (Abstract Base Classes):
   - O módulo 'abc' fornece funcionalidades para trabalhar com 
   classes abstratas em Python. Classes abstratas são classes que 
   não podem ser instanciadas diretamente e são usadas como base 
   para outras classes.
   
2. ABC (Abstract Base Class):
   - ABC é uma classe do módulo 'abc' que é usada como base para 
   definir classes abstratas em Python. Ao herdar da classe ABC, 
   uma classe é marcada como abstrata, o que significa que não pode 
   ser instanciada diretamente.
   
3. abstractmethod:
   - 'abstractmethod' é um decorador fornecido pelo módulo 'abc' que 
   é usado para marcar métodos como abstratos em uma classe abstrata. 
   Métodos marcados com '@abstractmethod' devem ser implementados por 
   qualquer classe que herde da classe abstrata. Isso permite definir 
   um contrato que subclasses devem seguir, garantindo que determinados 
   métodos sejam implementados.
   
No código fornecido:
- A classe Animal é marcada como abstrata ao herdar da classe ABC.
- Dois métodos, 'emitir_som' e 'info', são marcados como abstratos 
usando o decorador '@abstractmethod'. Isso significa que qualquer 
classe que herde de Animal deve implementar esses métodos.
- Tentar criar uma instância direta da classe Animal resultará em um 
erro TypeError, pois Animal é uma classe abstrata e não pode ser 
instanciada diretamente.

Em resumo, o código define uma classe abstrata Animal que serve como 
base para outras classes de animais, mas não pode ser instanciada 
diretamente. Ela exige que qualquer subclasse implemente os métodos 
'emitir_som' e 'info', garantindo que todas as subclasses forneçam esses 
comportamentos específicos.

----
O que é um Decorador?

Um decorador em Python é uma função que recebe outra função como 
argumento e retorna uma nova função, geralmente estendendo ou modificando 
o comportamento da função original de alguma maneira. Em outras palavras, 
os decoradores permitem adicionar funcionalidades a uma função existente 
sem alterar seu código diretamente.

Os decoradores são usados em várias situações, como:

Adicionar funcionalidades: Eles podem envolver uma função com código 
adicional, como registrar logs, verificar autorização, fazer tratamento 
de erros, entre outros.

Transformar a saída: Podem modificar o valor de retorno de uma função, 
convertendo-o em um formato diferente ou aplicando alguma transformação 
específica.

Validar entradas: Podem ser usados para verificar se os argumentos 
passados para uma função atendem a certos critérios antes que a função 
seja executada.

No contexto do código fornecido, o @abstractmethod é um exemplo de 
decorador. Ele é aplicado aos métodos emitir_som e info na classe 
abstrata Animal. Esses métodos são marcados como abstratos, o que significa 
que devem ser implementados por qualquer subclasse de Animal. O decorador 
@abstractmethod garante que uma exceção seja gerada se uma subclasse não 
implementar esses métodos, garantindo assim que todas as subclasses sigam 
fum contrato específico definido pela classe abstrata.
"""

from abc import ABC, abstractmethod

class Animal(ABC):  # Subclasses ABC to mark it as an abstract class
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def info(self):
        pass

# Attempting to create an instance of Animal will raise an error
try:
    animal_generico = Animal("Genérico", 5)
except TypeError as e:
    print("Error:", e)
