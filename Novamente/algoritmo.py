class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def e_vazio(self):
        return self.head is None
    
    def inserir_no(self, data):
        new_node = Node(data)
        if self.e_vazio():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node        
    
    def listar_tudo(self):
        atual = self.head
        while atual:
            print(atual.data, end=" <-> ")
            atual = atual.next
        print("None")
    
    def busca(self, data):
        atual = self.head
        while atual:
            if atual.data == data:
                return atual
            atual = atual.next
        return None
    
    def remover(self, data):
        atual = self.busca(data)
        if atual is None:
            return False
        if atual.prev:
            atual.prev.next = atual.next
        if atual.next:
            atual.next.prev = atual.prev
        if atual == self.head:
            self.head = atual.next
        if atual == self.tail:
            self.tail = atual.prev
        return True
    
    def limpar(self):
        self.head = None
        self.tail = None
            
            
dll = DoublyLinkedList()

dll.inserir_no(10)
dll.inserir_no(20)
dll.inserir_no(30)

dll.listar_tudo()

dll.remover(20)

dll.listar_tudo()
