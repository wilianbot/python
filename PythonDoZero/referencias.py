""" 
As variaveis funcionam como referências a objetos na memória, e não como ponteiros de memória
direta.

Isso significa que, ao atribuir uma varivel a outra, ambas possam a referencias o mesmo objeto.
"""

# Mutabel

a = [1, 2, 3]
b = a
b.append(5)

print(a)
print(b)

# Imutável

e = 5
c = e
c = 4

print(e)
print(c)