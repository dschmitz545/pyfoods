def ola(nome, cpf, idade=0, maisculo=False, *args, **kwargs):
    print(args)
    print(kwargs)
    if maisculo:
        msg = f"olá, {nome}".upper()
    else:
        msg = f"Olá, {nome}, {cpf}, idade: {idade}"
    print(msg)

ola("Lola", cpf=63593945)
ola("Luna", 9576975496,5,True) # Evitar usar esse tipo de chamada da função
ola("San", cpf=34598345, maisculo=True) # boa prática
ola("Zoe", cpf=6723465)

# duas formas de desempacotar uma tupla
pessoa = ['Diego',97834659, 32]
pessoa2 = ['Vini',97834659, 9]
nome, cpf, idade = pessoa2
ola(nome, cpf, idade)
ola(*pessoa)
    
pessoa3 = {
    'nome': 'Antonio',
    'cpf': '95885548698',
    'idade': 24
}
# desempacotando um dicionário
ola(**pessoa3)