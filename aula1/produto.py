from loja.modelos import Categoria, Produto

cadeira = Produto("cadeira", categoria=Categoria("Moveis"))
teclado = Produto("HyperX", categoria=Categoria("Eletronicos"))
print(cadeira.nome)
print(cadeira.categoria.nome)
print(teclado.nome)
print(teclado.categoria.nome)