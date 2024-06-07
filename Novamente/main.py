"""
Cada nó tem:

- Dados: O valor ou a informação que o nó armazena.

- Referências (ou ponteiros): Endereços que apontam para outros nós na estrutura. Em uma lista duplamente encadeada, cada nó tem:
    - Um ponteiro para o próximo nó (next).
    - Um ponteiro para o nó anterior (prev).
"""

# Lista encadeada está associado a Alocação Dinânica de memória

class Node:
    def __init__(self, data): # Método __init__ que aceita dois parâmetros self (a referência ao próprio objeto) e data (o valor que será armazenado no nó).
        self.data = data # Atribui o valaro de data ao atributo data do objeto.
        self.prev = None 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
            self.head = None
            self.tail = None
        
    def add_to_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
                    
    def add_to_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_from_start(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data
    
    def remove_from_end(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.head == self.tail:        
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
# Testando a implementação
dll = DoublyLinkedList()
dll.add_to_start(10)
dll.add_to_start(20)
dll.add_to_end(30)
dll.display()
print(dll.remove_from_start())
print(dll.remove_from_end())
dll.display()