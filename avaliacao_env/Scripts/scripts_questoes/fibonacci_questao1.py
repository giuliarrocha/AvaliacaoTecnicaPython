import sys

def fibonacci (n):
    if (n==0 or n==1):
        return n    
    return fibonacci(n-1) + fibonacci(n-2)

# Programa principal
n = int(sys.argv[1])
if (n>=0):
    resposta = fibonacci (n)
    print (resposta)
else:
    print ("Entrada incorreta. Digite um numero positivo.")