class Topology():
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0 for column in range(nodes)]
                      for row in range(nodes)]

    def print_routing_table(self):
        print("Source \tDestination \tDistance")
        for node in range(self.nodes):
            print(f"{self.src} \t{node} \t\t{self.dist[node]}")

    def min_distance_node(self, dist, visited):
        min_distance = float('inf')
        for v in range(self.nodes):
            if dist[v] < min_distance and not visited[v]:
                min_distance = dist[v]
                _min_distance_node = v

        return _min_distance_node

    def add_direct_connection(self, src, dest, weight):
        self.graph[src][dest] = self.graph[dest][src] = weight

    def dijkstra(self, src):
        self.src = src
        self.dist = [float('inf')] * self.nodes
        self.dist[src] = 0
        visited = [False] * self.nodes

        for _ in range(self.nodes):
            u = self.min_distance_node(self.dist, visited)
            visited[u] = True
            for v in range(self.nodes):
                if self.graph[u][v] > 0 and not visited[v] and self.dist[v] > self.dist[u] + self.graph[u][v]:
                    self.dist[v] = self.dist[u] + self.graph[u][v]


network = Topology(int(input("Enter number of nodes in the topology: ")))
num_edges = int(input("Enter number of edges: "))

for i in range(num_edges):
    src, dest, cost = list(map(int, input("Enter [src] [dest] [weight]: ").split(' ')))
    network.add_direct_connection(src, dest, cost)

src = int(input("Enter [src] to find costs: "))

network.dijkstra(src)
network.print_routing_table()