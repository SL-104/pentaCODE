import heapq

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = {}

    def add_edge(self, neighbor, weight):
        self.adjacency_list[neighbor] = weight

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].add_edge(to_vertex, weight)
        self.vertices[to_vertex].add_edge(from_vertex, weight)  # Undirected graph

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]
        shortest_path_tree = {}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].adjacency_list.items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_path_tree[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, shortest_path_tree

    def get_shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return None, None, []

        distances, shortest_path_tree = self.dijkstra(start_vertex)
        if distances[end_vertex] == float('inf'):  # No path exists
            return None, None, []

        path = []
        edges_in_path = []  # This will hold the edges in the shortest path
        current_vertex = end_vertex

        while current_vertex != start_vertex:
            path.append(current_vertex)
            previous_vertex = shortest_path_tree.get(current_vertex)
            if previous_vertex is None:
                return None, None, []
            
            # Add the edge to the list of edges in the shortest path
            edges_in_path.append((previous_vertex, current_vertex))
            current_vertex = previous_vertex

        path.append(start_vertex)
        return path[::-1], distances[end_vertex], edges_in_path



# Create the train graph
train_graph = Graph()


# Add edges with weights (LRT 1)
train_graph.add_edge("Fernando Poe Jr.", "Balintawak", 1.870)
train_graph.add_edge("Balintawak", "Monumento", 2.250)
train_graph.add_edge("Monumento", "5th Avenue", 1.087)
train_graph.add_edge("5th Avenue", "R. Papa", 0.954)
train_graph.add_edge("R. Papa", "Abad Santos", 0.660)
train_graph.add_edge("Abad Santos", "Blumentritt", 0.927)
train_graph.add_edge("Blumentritt", "Tayuman", 0.671)
train_graph.add_edge("Tayuman", "Bambang", 0.618)
train_graph.add_edge("Bambang", "Doroteo Jose", 0.648)
train_graph.add_edge("Doroteo Jose", "Carriedo", 0.685)
train_graph.add_edge("Carriedo", "Central Terminal", 0.725)
train_graph.add_edge("Central Terminal", "United Nations", 1.214)
train_graph.add_edge("United Nations", "Pedro Gil", 0.754)
train_graph.add_edge("Pedro Gil", "Quirino", 0.794)
train_graph.add_edge("Quirino", "Vito Cruz", 0.827)
train_graph.add_edge("Vito Cruz", "Gil Puyat", 1.061)
train_graph.add_edge("Gil Puyat", "Libertad", 0.730)
train_graph.add_edge("Libertad", "EDSA", 1.010)
train_graph.add_edge("EDSA", "Baclaran", 0.588)
train_graph.add_edge("Baclaran", "Redemptorist-Aseana", 0.869)
train_graph.add_edge("Redemptorist-Aseana", "MIA Road", 1.303)
train_graph.add_edge("MIA Road", "PITX", 1.141)
train_graph.add_edge("PITX", "Ninoy Aquino Avenue", 1.393)
train_graph.add_edge("Ninoy Aquino Avenue", "Dr. Santos", 1.646)


# LRT 2
train_graph.add_edge("Antipolo", "Marikina–Pasig", 2.232)
train_graph.add_edge("Marikina–Pasig", "Santolan", 1.795)
train_graph.add_edge("Santolan", "Katipunan", 1.970)
train_graph.add_edge("Katipunan", "Anonas", 0.955)
train_graph.add_edge("Anonas", "Araneta Center–Cubao(LRT)", 1.438)
train_graph.add_edge("Araneta Center–Cubao(LRT)", "Betty Go-Belmonte", 1.164)
train_graph.add_edge("Betty Go-Belmonte", "Gilmore", 1.075)
train_graph.add_edge("Gilmore", "J. Ruiz", 0.928)
train_graph.add_edge("J. Ruiz", "V. Mapa", 1.234)
train_graph.add_edge("V. Mapa", "Pureza", 1.357)
train_graph.add_edge("Pureza", "Legarda", 1.389)
train_graph.add_edge("Legarda", "Recto", 1.050)
train_graph.add_edge("Recto", "Doroteo Jose", 0.030)

# LRT 3 (MRT Line)
train_graph.add_edge("North Avenue", "Quezon Avenue", 1.200)
train_graph.add_edge("Quezon Avenue", "GMA–Kamuning", 1.000)
train_graph.add_edge("GMA–Kamuning", "Araneta Center–Cubao(MRT)", 1.900)
train_graph.add_edge("Araneta Center–Cubao(MRT)", "Santolan–Annapolis", 1.500)
train_graph.add_edge("Santolan–Annapolis", "Ortigas", 2.300)
train_graph.add_edge("Ortigas", "Shaw Boulevard", 0.800)
train_graph.add_edge("Shaw Boulevard", "Boni", 1.000)
train_graph.add_edge("Boni", "Guadalupe", 0.800)
train_graph.add_edge("Guadalupe", "Buendia", 2.000)
train_graph.add_edge("Buendia", "Ayala", 0.950)
train_graph.add_edge("Ayala", "Magallanes", 1.200)
train_graph.add_edge("Magallanes", "Taft Avenue", 2.050)

# Transfer points
train_graph.add_edge("Doroteo Jose", "Recto", 0.030)
train_graph.add_edge("Araneta Center–Cubao(LRT)", "Araneta Center–Cubao(MRT)", 0.050)

