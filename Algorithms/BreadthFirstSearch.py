import math
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
        
class BFS:
    def __init__(self, graph, starting="",destination=""):
        self.g = graph
        self.a = starting
        self.b = destination
        self.color = dict()
        self.d = dict()
        self.pre = dict()
    def set_graph(self, graph):
        self.g = graph
    def set_starting(self, sp):
        self.a = sp
    def set_destination(self, dp):
        self.b = dp
    def shortest_path(self):
        for v in self.g:
            self.color[v] = "white"
            self.d[v] = math.inf
            self.pre[v] = "Null"
        Q = Queue()
        self.color[self.a] = "green"
        self.d[self.a] = 0
        Q.enqueue(self.a)
        while not Q.isempty():
            u = Q.dequeue()
            for v in self.g[u]:
                if self.color[v] == "white":
                    self.color[v] = "green"
                    Q.enqueue(v)
                    self.d[v] = self.d[u] + 1
                    self.pre[v] = u
            color = "red"
        temp = self.b
        self.shortestpath = list()
        while temp != "Null":
            self.shortestpath.append(temp)
            temp = self.pre[temp]
        return self.shortestpath
