class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def vazia(self):
        return self.cabeca is None

    def inserir_elemento(self, dado):
        novo_nodo = Nodo(dado)
        if self.vazia():
            self.cabeca = self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            novo_nodo.anterior = self.cauda
            self.cauda = novo_nodo

    def listar_tudo(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

    def busca_elemento(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dado == dado:
                return atual
            atual = atual.proximo
        return None

    def remover_elemento(self, dado):
        atual = self.busca_elemento(dado)
        if atual is None:
            return False
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior
        return True

    def liberar_lista(self):
        self.cabeca = None
        self.cauda = None
        print("Lista liberada")

# inicializa
minha_lista = ListaDuplamenteEncadeada()

# inserção de elementos
minha_lista.inserir_elemento(10)
minha_lista.inserir_elemento(20)
minha_lista.inserir_elemento(30)

# Listagem inicial
print("Lista inicial:")
minha_lista.listar_tudo()

# Loop para procurar na lista
while True:
    try:
        dado = int(input("Escolha um elemento (ou digite 0 para sair): "))
        if dado == 0:
            break
        resultado = minha_lista.busca_elemento(dado)
        if resultado:
            print(f'Elemento {dado} encontrado.')
        else:
            print(f'Elemento {dado} não encontrado.')
    except ValueError:
        print("Por favor, insira um número válido.")

print("Encerrando o programa.")
