print("EXIBIDOR DE LISTA")  # questao 1

n1 = int(input("Insira qualquer número inteiro! "))
n2 = int(input("Insira qualquer número inteiro! "))
n3 = int(input("Insira qualquer número inteiro! "))
n4 = int(input("Insira qualquer número inteiro! "))
n5 = int(input("Insira qualquer número inteiro! "))

lista = [n1, n2, n3, n4, n5]

print("Listagem:", lista)

# questao 2
exibir_numero = lista[0]
exibir_numero1 = lista[2]
exibir_numero2 = lista[4]

print("Primeiro número é", exibir_numero, "Terceiro é", exibir_numero1, "Já o último é", exibir_numero2)

# questao 3
print("Alteração de número!")
pos = int(input("Escolha a posição (1, 2, 3, 4 ou 5): ")) - 1
valor = int(input("Qual será o novo número? "))

lista[pos] = valor

print("Lista alterada:", lista)

novo_numero = int(input("Insira mais um número para adicionar à lista: "))
lista.append(novo_numero)

print("Lista atualizada:", lista)
