class Animal:
    # atributos de classe(variavel)
    planeta = "Terra"
    _animal_nasceu = False

    @property # por convencao, atributos que começam com _, são privados, porém, nada impede de acessar fora da classe esse atributo
    def nasceu(self):
        return self._animal_nasceu
    
    # método(função)
    def nascer(self): # por padrão, ele precisa receber um parametro especial, como primeiro argumento
        self._animal_nasceu = True
        print(f"Oi eu nasci no planeta {self.planeta}") # ao inves de self, poderia ser qualquer nome, this, outro_nome

    def comer(self):
        print("Estou comendo")

class Mamifero(Animal):
    def comer(self):
        print("Eu estou tomando leite...")

class Oviparos(Animal):
    def nascer(self):
        print(f"Acebei de quebrar o ovo no planeta {self.planeta}")

class Especial(Mamifero, Oviparos):
    def nadar(self):
        print("Estou nadando")

Tubarao = Animal()
Tubarao.nascer()

gato = Mamifero()
gato.comer()
#print(gato.nasceu())
print(gato.nasceu)
gato.nascer()
print(gato.nasceu)
#print(gato.nasceu())


jacare = Oviparos()
jacare.nascer()

jubarte = Especial()
jubarte.nadar()
print(Especial.mro())