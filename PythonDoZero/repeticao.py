notas = [] ## Criar uma lista

# For para ler as notas
for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)  
      


print("Quantidade de notas", len(notas))


# For para mostrar as notas
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)
    
    
    
# ===========Outra alternativa com While===============

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    notas = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    # alternativa: contador += 1
    contador = contador + 1
    
print("quantidade de notas", len(notas))

contador = 1

while contador <= len(notas):
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)
