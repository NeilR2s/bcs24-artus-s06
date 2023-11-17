# linked list is a linear data stucture where each element is a seperate object called node
# a node contains two items: data and reference (next node)

class Node:
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade
        self.next = None

class Stack:
    def __init__(self,):
        self.top = None

    def is_empty (self):
        return self.top is None

    def push (self, name, grade):
        new_node = Node(name, grade)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return new_node
        pop_node = self.top
        self.top = self.top.next
        return pop_node.name, pop_node.grade

    def peek(self):
        if self.is_empty():
            return None
        return self.top.name, self.top.grade
    
#create an empty stack

s = Stack()

s.push("Pia", 98)
s.push("Mhel", 100)
s.push("Jungkook", 75)

print(s.peek())
print(s.pop())
print(s.pop())
print(s.peek())

        
