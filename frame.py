class Frame:
    def __init__(self,max_locals,max_stack):
        self.locals=[0]*max_locals
        self.stack=[]
        self.max_stack=max_stack
    
    def push(self,value):
        if len(self.stack) >= self.max_stack:
            raise Exception("Operand stack overflow")
        self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            raise Exception("Operand stack underflow")
        return self.stack.pop()