# Preencha uma lista com 10 números digitados pelo usuário e exiba:
# o maior número
# o menor número
# a média dos números
# todos os números menores que a média calculada

lista = []
for i in range(10):
    num = int(input("Digite um número:"))
    lista.append(num)

    print("O menor número da lista é:", min(lista))
    print("O maior número da lista é:", max(lista))
    media = sum(lista) / len(lista)
    print("A média dos valores da lista é:", media)

for i in lista:
    if i < media:
        print(i)
