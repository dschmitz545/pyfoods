z = 0
y = 10

try:
    y.upper()
    print(y // z)
except AttributeError as err:
    print("mais um erro, ", str(err))
except ZeroDivisionError as err:
    print("deu erro, tente novamente. ", str(err))
