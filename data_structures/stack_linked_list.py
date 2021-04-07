
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self._size = 0


    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size+=1



    def pop(self):
        result = self.isEmpty()
        if not result:
            node = self.top.data
            self.top = self.top.next
            self._size-=1
            return node
        raise IndexError('empty stack')
                    


    def isEmpty(self):
        if self._size == 0:
            return True
        return False


    def peek(self):
        result = self.isEmpty()
        if not result:
            return self.top.data
        raise IndexError('empty stack')


    def __len__(self):
        return self._size

    # parênteses balanceados:
    # cada símbolo de abertura, tem um símbolo de fechamento correspondente.
    # exemplo: {[(])}
    # 1. adiciona-se na pilha todos os símbolos de abertura
    # 2. quando chegar em um símbolo de fechamento, dá-se um pop() na pilha, e se esse símbolo for correspondente ao símbolo de fechamento, até aí está balanceada a expressão.
    # essa expressão não está balanceada: (]

    def balanced(self, expression):
        for i in range(len(expression)):
            if expression[i] in "([{":
                self.push(expression[i])
            elif expression[i] in ")]}":
                opened = self.peek()
                closed = expression[i]
                result = self.arePairs(opened, closed)
                if result:
                    self.pop()
                else:
                    return 'Not balanced'
            

    
    def arePairs(self, opened, closed):
        if opened == "(" and closed == ")":
            return True
        elif opened == "[" and closed == "]":
            return True
        elif opened == "{" and closed == "}":
            return True
        return False

    

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r


    def __str__(self):
        return self.__repr__()

