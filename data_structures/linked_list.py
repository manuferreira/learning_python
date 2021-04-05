
class Node():
    def __init__(self, data):
        self.data = data #dado
        self.next = None #ponteiro


class linkedList():
    def __init__(self):
        self.head = None #inicialmente a lista é vazia
        self._size = 0



    def __len__(self):
        return self._size

    
    def index(self, elem): # retorna o índice do elemento procurado
        pointer = self.head
        count = 0
        while pointer:
            if pointer.data == elem:
                return count
            count+=1
            pointer = pointer.next
        raise ValueError(f'{elem} is not in list')



    def append(self, elem):
        if self.head: #checamos se há algum elemento na lista
            pointer = self.head
            while pointer.next: #enquanto o elemento atual não for o último, continuamos percorrendo
                pointer = pointer.next
            pointer.next = Node(elem) # associamos ao next da última posição
        else:
            self.head = Node(elem)

        self._size+=1



    def _getnode(self, index): # método que procura o elemento que está em determinado índice
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer



    def insert(self, index, elem): #inserir em qualquer posição da lista, a partir de um índice
        if index == 0: # caso se queira inserir na head
            new_elem = Node(elem)
            new_elem.next = self.head
            self.head = new_elem

        else:
            ancestor = self._getnode(index-1) #pegamos o elemento que está no índice anterior, ou seja, o elemento antecessor
            new_elem = Node(elem)
            new_elem.next = ancestor.next
            ancestor.next = new_elem
        self._size+=1



    def remove(self, elem):
        # checamos se a lista está vazia
        if self.head == None:
            raise ValueError(f'{elem} not in list')

        elif self.head.data == elem:
            self.head = self.head.next
            self._size=-1
            return True

        else:
            ancestor = self.head # uma referência ao antecessor
            pointer = self.head.next # uma referência ao elemento atual que vamos percorrer
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next #conectamos o antecessor ao sucessor do elemento que removemos
                    pointer.next = None
                    self._size -= 1
                    return True
                else:
                    ancestor = pointer
                    pointer = pointer.next # o pointer está sempre uma posição a frente do antecessor

        raise ValueError(f'{elem} is not in list')



    def traverse(self):
        r = ''
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + '-> '
            pointer = pointer.next
        return r
        

