
class Stack:
    
    def __init__(self,):
        self.min_stack = []
        self.stack = []
        
    def min(self):
        if not self.min_stack:
            raise 'min_stack is EMPTY'
        
        return self.min_stack[-1]
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
            return
        
        
        if value < self.min():
            print(self.min_stack)
            print(f'min: {self.min()}')
            self.min_stack.append(value)
                    
    
    def pop(self,):
        if not self.stack:
            return 'EMPTY STACK'
        
        if self.top() == self.min():
            print(f'top == min: {self.top()}')
            self.min_stack.pop(-1)
        
        return self.stack.pop(-1)

    def top(self,):
        if self.stack:
            return self.stack[-1]
        
       
       
def SelectionSort_by_3stacks(stack1):
    if not stack1:
        return
    stack2 = []
    stack3 = []
    
    while stack1:
        global_min = stack1.pop()
        while stack1:
            # print(f'global_min: {global_min}')
            if stack1[-1] < global_min:
                stack2.append(global_min)
                global_min = stack1.pop()
            else:
                stack2.append(stack1.pop())
        stack3.append(global_min)
        
        print(f'left-bound: {stack3} |    {stack2}')
        while stack2:
            stack1.append(stack2.pop())
    return stack3
            
        

if __name__ =="__main__":
    # stack = Stack()
    # stack.push(3)
    # stack.push(1)
    # stack.push(2)
    # stack.push(4)
    # stack.push(-7)
    # stack.push(-8)

    # print(stack.min())
    
    # stack.pop()
    # print(stack.min())
    # stack.pop()
    # print(stack.min())
    # stack.pop()
    # print(stack.min())
    # stack.pop()
    # print(stack.min())
    # stack.pop()
    # print(stack.min())
    # stack.pop()
    # print(stack.min())
                
        
    stack1 = [15,23,0,3, 8,7,21]
    sorted_array = SelectionSort_by_3stacks(stack1)
    print(sorted_array)
    
    
    