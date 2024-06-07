import os # Usada para interagir com o sistema operacional

mensagens = []

nome = input("Nome: ")

while True:
    
    # limpando terminal
    os.system("clear")
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m["nome"], "-", m["texto"])
            
    print("__________________________")
    
    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim" or texto == "FIM" :
        break
    
    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })