def multiplicar(a,b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a+ multiplicar(a, b -1)




if  __name__== "__main__":
    resultado=multiplicar(3, 6)
    print(resultado)
