# Well, the book doesn't demonstrate any practical 
# implementation of linked lists, so I had to do my own

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

    def get_value(self):
        if not self.is_empty():
            return self.value
        raise IndexError('The node is empty.')

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value

    def is_empty(self):
        return self.value is None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.first: Node | None = None
        self.last: Node | None = None
        self.lenght = 0

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = self.first
        else:
            self.last.set_next(new_node)
            self.last = new_node
        self.lenght += 1

    def left_push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = self.first
        else:
            new_node.set_next(self.first)
            self.first = new_node
        self.lenght += 1

    def pop(self):
        last_node: Node | None = self.last
        self.last = None

        if last_node is None:
            raise IndexError('The list is empty.')

        return last_node

    def pop_left(self):
        first_node = self.first
        if first_node is None:
            raise IndexError('The list is empty.')
        elif self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.get_next()
        return first_node

    def index_of(self, target):
        if self.is_empty():
            raise IndexError('The list is empty')

        aux = self.first

        for n in range(self.lenght):
            if aux.get_value() == target:
                return n
            aux = aux.get_next()

        raise ValueError(f'{target} is not in list')

    def get_in_index(self, value: int):
        if self.is_empty():
            raise IndexError('The list is empty')

        aux = self.first

        for n in range(value+1):
            if n == value:
                return aux.get_value()
            aux = aux.get_next()

    def insert(self, value, index):
        if self.is_empty():
            raise IndexError('The list is empty')
        elif index > self.lenght or index < 0:
            raise IndexError('Index out of range')

        new_node = Node(value)
        aux = self.first
        for n in range(index):
            aux = aux.get_next()
        old_node = aux.get_next()
        new_node.set_next(old_node)
        aux.set_next(new_node)
        self.lenght += 1

    def remove(self, index):
        if self.is_empty():
            raise IndexError('The list is empty')
        elif index > self.lenght or index < 0:
            raise IndexError('Index out of range')
        elif index == 0:
            self.pop_left()
            return True

        aux = self.first
        for n in range(index-1):
            aux = aux.get_next()
        aux_next = aux.get_next()
        next_in_new_chain = aux_next.get_next()
        aux.set_next(next_in_new_chain)
        return True

    def reset(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def is_empty(self):
        return self.first is None

    def __str__(self) -> str:
        string = '['
        value = self.first
        while value is not None:
            if value.get_next() is None:
                string += f'{str(value.get_value())}'
            else:
                string += f'{str(value.get_value())}, '
            value = value.get_next()
        string += ']'
        return string
