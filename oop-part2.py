"""
Este programa apresenta um exemplo de herança em Python. 
Herança é um conceito de programação orientada a objetos que 
permite criar uma nova classe usando detalhes de uma classe 
existente. 

A nova classe, chamada de subclasse, pode herdar atributos e 
métodos da classe existente, chamada de superclasse.

No exemplo abaixo, temos quatro classes: Animal, Nadador, 
Cachorro e Gato. A classe Animal é a superclasse base, que 
possui métodos e atributos compartilhados por todos os 
animais. A classe Nadador é uma classe adicional que 
define o comportamento de nadar e é destinada a ser herdada 
por animais que são nadadores. As classes Cachorro e Gato 
são subclasses que herdam da classe Animal e também da classe 
Nadador, indicando que tanto os cachorros quanto os gatos são 
animais e nadadores.

Agora, vamos explicar cada classe e seu propósito:

1. Classe Animal:
   - Possui um construtor que inicializa o nome e a idade do 
   animal.
   - Define um método 'emitir_som()' que é destinado a ser 
   sobrescrito por subclasses para representar os diferentes 
   sons emitidos pelos animais.
   - Define um método 'info()' para imprimir informações 
   básicas do animal.

2. Classe Nadador:
   - Possui um construtor que inicializa o estilo de nado do 
   nadador.
   - Define um método 'nadar()' para indicar que o animal está 
   nadando com um estilo específico.

3. Classe Cachorro:
   - Herda de Animal e Nadador.
   - Além de inicializar o nome, idade e estilo de nado, também 
   inicializa a raça do cachorro.
   - Sobrescreve o método 'emitir_som()' para representar o som 
   característico de um cachorro.

4. Classe Gato:
   - Herda de Animal e Nadador.
   - Além de inicializar o nome, idade e estilo de nado, também 
   inicializa a cor do gato.
   - Sobrescreve o método 'emitir_som()' para representar o som 
   característico de um gato.

5. Classe Passaro:
   - Herda apenas de Animal.
   - Além de inicializar o nome e a idade, também inicializa a 
   espécie do pássaro.
   - Sobrescreve o método 'emitir_som()' para representar o som 
   característico de um pássaro.

Para criar instâncias das classes e demonstrar o uso do código, 
são criados quatro animais: um animal genérico, um cachorro, um 
gato e um pássaro. Em seguida, o método 'info()' é chamado para 
exibir informações sobre cada animal.
"""

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade  

    def emitir_som(self):
        pass  

    def info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")  


class Nadador:
    def __init__(self, estilo_nado):
        self.estilo_nado = estilo_nado  

    def nadar(self):
        print(f"{self.nome} está nadando com o estilo {self.estilo_nado}!")  


class Cachorro(Animal, Nadador):
    def __init__(self, nome, idade, raca, estilo_nado):
        Animal.__init__(self, nome, idade)  
        Nadador.__init__(self, estilo_nado)  
        self.raca = raca  

    def emitir_som(self):
        print("Au Au!")  


class Gato(Animal, Nadador):
    def __init__(self, nome, idade, cor, estilo_nado):
        Animal.__init__(self, nome, idade)  
        Nadador.__init__(self, estilo_nado)  
        self.cor = cor  

    def emitir_som(self):
        print("Miau!")  


class Passaro(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)  
        self.especie = especie  

    def emitir_som(self):
        print("Piu Piu!")  


animal_generico = Animal("Genérico", 5)  
cachorro = Cachorro("Rex", 3, "Labrador", "cachorrinho")  
gato = Gato("Bolinha", 2, "Branco", "gatinho")  
passaro = Passaro("Piu", 1, "Canário")  

animal_generico.info()  
cachorro.info()
gato.info()
passaro.info()