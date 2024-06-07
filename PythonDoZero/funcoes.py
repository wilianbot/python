def minha_funcao(valor1, valor2): # Função
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    
    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)
    
    texto = (input("Continuar? y / n :"))
    if texto == "n":
        break