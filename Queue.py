class Queue:
    def __init__(self):
        self.q = list()
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        return self.q.pop(0)
    def isempty(self):
        if not self.q: return True
        else: return False
