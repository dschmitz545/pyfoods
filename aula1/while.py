counter = 0
while counter < 11:

    print(f"hello world {counter}")
    counter += 1
    if counter == 10:
        break

continuar = 'sim'
while continuar == 'sim':
    print(input("Qual seu nome? "))
    continuar = input("continuar? sim ou não ")
