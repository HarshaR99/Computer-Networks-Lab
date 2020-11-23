
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, dist):
        print("Vertex\tDistance")
        for i in range(self.V):
            print(str(i)+"\t"+str(dist[i]))

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] < float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        self.print_solution(dist)

def simulate():
    matrix = []
    n= int(input("Enter number of nodes: "))
    print("Enter the adjacency matrix:")
    for i in range(n):
        m = list(map(int,input().strip().split()))
        matrix.append(m)
    g=Graph(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                g.add_edge(i,j,1)
    for i in range(n):
        g.bellman_ford(i)


simulate()
