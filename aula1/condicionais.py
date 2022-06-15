num = input("digite um numero: ")

if num == '1':
    print("digitou 1")
elif num == '2':
    print("digitou 2")
elif num == '3':
    print("digitou 3")
elif num == '4':
    print("digitou 4")
elif num == '5' and num == '5':
    print("digitou 5")
elif num == '6' or num == '7':
    input("digitou 6")

else:
    print("digitou outra coisa")

"""
bloco de comentário

ternário
"""
if num == '1' or num == '2' or num == '3' or num == '4' or num == '0':
    online = True

else:
    online = False

print("Estou online" if online else "Estou offline")
