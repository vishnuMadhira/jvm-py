class JVM:
    def __init__(self):
        self.frames=[]
    
    def push_frame(self,frame):
        self.frames.append(frame)
    
    def pop_frame(self):
        return self.frames.pop()
    
    def current_frame(self):
        return self.frames[-1]