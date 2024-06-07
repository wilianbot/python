class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None
        
    # ============= Inicialização - Barrela ========
    
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        
    # ============= Verifica se a lista esta vazia - Barrela ========
    
    def vazia(self):    
        return self.cabeca is None
      
    # ============= Inserção de elementos - Barrela ========
    
    def inserir_elemento(self, dado): 
        novo_nodo = Nodo(dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            
        else:
            self.cauda.proximo = novo_nodo
            novo_nodo.anterior = self.cauda
            self.cauda = novo_nodo
            
    # ============= Listagem - Wilian ========
            
    def listar_tudo(self): 
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")
        
        
    # ============= Busca de um elementro na lista - Rudivan ========
    
    def busca_elemento(self, dado):
        atual = self.cabeca
        while atual:
            if atual.dado == dado:
                return atual
            atual = atual.proximo
        return None

    
    # ================ Remove um elemento da lista - Wilian ===========
    
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
    
    # ======================= Liberar a lista - Wilian =================== 
        
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

# Listagem
minha_lista.listar_tudo() 

# Remover elemento
minha_lista.remover_elemento(30)


print("Lista Inicial:")
# Listagem
minha_lista.listar_tudo() 


#loop para procurar na lista 
while True:
    try: #pede para selecionar um elemento ou sair
        dado = int(input("Escolha um objeto (ou digite 0 para sair): "))
        if dado == 0: #função para sair
            break
        resultado = minha_lista.busca_elemento(dado)
        if resultado: # o elemento selecionado
            print(f'Elemento {dado} encontrado.')
             
        else: # se o elemento selecionado n existir vai printar isso e vai pedir para selecionar um outro
            print(f'Elemento {dado} não encontrado.')
    except ValueError:
        print("Por favor, insira um número válido.")

print("Encerrando o programa.")


