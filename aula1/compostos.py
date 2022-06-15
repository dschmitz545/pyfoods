# Listas - permite alteração
cores = ["red", "green", "blue"]
numeros = [1, 2, 3]
mistura = [1, "diego", 2, 5, True, cores, numeros, ["a", "b", "c"]]

cores.append("cyan")  # entra como ultimo elemento
print(cores)
cores.insert(1, "black")  # define atravez do indice, a posição na lista
print(cores)
cores.remove("blue")
print(cores)

# Tuplas - não permite alteração
identidade = ("Diego", "067876456-89", 34)
print(f"Nome: {identidade[0]}")
print(f"CPF: {identidade[1]}")
print(f"idade: {identidade[1]}")

# desempacotamento de tuplas
# pode ser feito com listas ou qualquer sequencia
# (explode ou unpacket)
nome, cpf, idade = identidade
print(nome, cpf, idade)

# Dicionário - (igual ao array associativo, hasmap) - Object do javascript
# é uma sequencia igual a lista, tupla, porem mutavel

pessoa = {
    "nome": "Vini",
    "cpf": "015024547-89",
    "idade": 12
}

# Diferença na hora do acesso
# na lista usa o indice,
# aqui usa a chave.

pessoa["idade"] = 10
pessoa["canal"] = "dschmitz.dev"

print(f"Ola, o(a) {pessoa['nome']} tem {pessoa['idade']} anos de idade");

### Iteração

for cor in cores:
    print(cor.upper())

for letra in cores[0]:
    print(letra.capitalize())
    print("Vinicius"[-1])
    print("Vinicius"[-2])
    print("Vinicius"[-3])
    print("Vinicius"[0])

for letr in "Vinicius":
    if letr == 'i':
        continue
    print(letr)

# List - Comprehension
letra1: str = "Vinicius Zaffonato Schmitz"
print([letr1 for letr1 in letra1])

# lits comprehension filtered
print([letr1 for letr1 in letra1 if letr1 != 'i'])

# iteração em objeto(dicionario)

for chave in pessoa:
    print(chave, ":", pessoa[chave])

for chave, valor in pessoa.items(): # retorna uma tupla
    print(chave, valor)