# Suponha que você queira contar o número de elementos em uma lista que satisfazem uma condição específica.

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Condição: contar apenas números maiores que 25
condicao = 25

# Inicialize o contador
contador = 0

# Percorra a lista e conte os números que satisfazem a condição
for numero in numeros:
    contador += numero > condicao

# Imprima o resultado
print(f'O número de elementos maiores que {condicao} é: {contador}')

"""
Alternativa menos eficiente

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Condição: contar apenas números maiores que 25
condicao = 25

# Inicialize o contador
contador = 0

# Percorra a lista e verifique a condição para cada elemento
for numero in numeros:
    if numero > condicao:
        contador += 1

# Imprima o resultado
print("O número de elementos maiores que", condicao, "é:", contador)

"""