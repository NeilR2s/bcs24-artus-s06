# Pop operation
class PopStack:
    def __init__ (self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size
        
    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top +=1
                self.stack.append(data)
                #check if succesfully push
                return True
            else:
                #element is already in stack
                return False
        
        else: 
            #stack is full or overflow
            return "Stack overflow"
    
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -=1
            return popped_element
        else:
            return "Stack Underflow"
            
    def display_elements(self):
        if self.is_empty():
            print ("Stack Underflow")
        else:
            print("Elements in stack list: ")
            for i in range (self.top +1):
                print (self.stack[i])
            
#create a stack with a maximum of 5
stack = PopStack(5)

print(stack.push("Pia"))
print(stack.push("Rome"))
print(stack.push("Jin"))
print(stack.push("V"))
print(stack.push("Jimin"))

stack.display_elements()

#removing elements one by one from stack
print("Popping element one by one: ")
while not stack.is_empty():
    popped = stack.pop()
    print("Remove Element ", popped)
stack.display_elements