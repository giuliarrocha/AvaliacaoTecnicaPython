import sys

def fibonacci (n):
    if (n==0 or n==1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Programa principal
resposta = fibonacci (int(sys.argv[1]))
print (resposta)