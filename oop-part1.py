"""
Demonstrates every aspect of OOP in Python
"""

# Definindo uma classe chamada Animal
class Animal:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de instância
    def emitir_som(self):
        pass  # Este método será sobrescrito em classes filhas

    # Método de instância
    def info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Definindo uma subclasse de Animal chamada Cachorro
class Cachorro(Animal):
    # Método construtor
    def __init__(self, nome, idade, raca):
        # Chamando o construtor da classe pai
        super().__init__(nome, idade)
        self.raca = raca

    # Sobrescrevendo o método emitir_som da classe pai
    def emitir_som(self):
        print("Au Au!")

# Definindo uma subclasse de Animal chamada Gato
class Gato(Animal):
    # Método construtor
    def __init__(self, nome, idade, cor):
        # Chamando o construtor da classe pai
        super().__init__(nome, idade)
        self.cor = cor

    # Sobrescrevendo o método emitir_som da classe pai
    def emitir_som(self):
        print("Miau!")

# Instanciando objetos das classes
animal_generico = Animal("Genérico", 5)
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Bolinha", 2, "Branco")

# Chamando métodos dos objetos
animal_generico.info()
animal_generico.emitir_som()

cachorro.info()
cachorro.emitir_som()

gato.info()
gato.emitir_som()
