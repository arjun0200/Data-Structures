from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class Linkedlist:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
    def remove_duplicates(self):
        if self.head is None:
            return
    
        current_node = self.head
        prev_node = None
    
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
    
        self.tail = prev_node  
        return self.head
# ll = Linkedlist()
# ll.generate(10,0,99)
# print(ll)
# print(len(ll))
# print([node.value for node in ll])
# ll.remove_duplicates()
