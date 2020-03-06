# Faça um programa que simule um lançamento de dados.
# Lance o dado 10 vezes e armazene os resultados em uma lista.
# Depois, informe quantas vezes cada número foi sorteado.
# Utilize o módulo random : import random..(n = random.randint(1, 6))


from random import randint
lista = []
for i in range(10):
    lista.append(randint(1, 6))
print(lista)

for i in range(1, 7):
    print("Némero", i, " aparece", lista.count(i), "vezes")
