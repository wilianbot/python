salario = float(input("Informe sua renda:"))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programdor pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")