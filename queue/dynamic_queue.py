
class Queue:
    def __init__(self):
        self.head_pointer =-1 
        self.queue =[] 

    def push(self, item):
        if item:
            item = [item]
            self.queue = item + self.queue
            self.head_pointer +=1
        pass

    def pop(self):
        if self.head_pointer !=-1:
            item = self.queue[self.head_pointer]
            self.queue = self.queue[:self.head_pointer]
            self.head_pointer -=1
            return item
        else:
            return None

    def peek(self):
        if self.head_pointer !=-1:
            return self.queue[self.head_pointer]
        pass

    def size(self):
        return self.head_pointer -1
        pass
