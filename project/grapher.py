import heapq


class Graph:
    def __init__(self):
        self.graph = dict()

    def has_vertex(self,vertex):
        return vertex in self.graph

    def has_edge(self,vertex1, vertex2):
        if self.has_vertex(vertex1) and self.has_vertex(vertex2):
            edges = self.graph[vertex1]
            for e in edges:
                for v in e:
                    if vertex2 == v:
                        return True
        return False

    def get_weight(self,vertex1,vertex2):
        found = False
        if self.has_edge(vertex1, vertex2):
            i = -1
            edges = self.graph[vertex1]
            for e in edges:
                i += 1
                if vertex2 == e[0]:
                    return self.graph[vertex1][i][1]
        return found

    def update_edge_weight(self,vertex1, vertex2, weight):
        if self.has_edge(vertex1, vertex2):
            i = -1
            found = False
            edges = self.graph[vertex1]
            for e in edges:
                i += 1
                if vertex2 == e[0]:
                    found = True
                    break;
            if found:
                self.graph[vertex1][i][1] = weight
            i = -1
            found = False
            edges = self.graph[vertex2]
            for e in edges:
                i += 1
                if vertex1 == e[0]:
                    found = True
                    break;
            if found:
                self.graph[vertex2][i][1] = weight

    def get_neighbours(self,vertex):
        neighbours = list()
        if self.has_vertex(vertex):
            for neighbour in self.graph[vertex]:
                neighbours.append(neighbour)
        return neighbours

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = list()

    def get_neighbour_names(self,vertex):
        neighbour_names = list()
        if self.has_vertex(vertex):
            for neighbour in self.graph[vertex]:
                neighbour_names.append(neighbour[0])
        return neighbour_names


    def add_edge(self,vertex1, vertex2, weight, type):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        if self.has_edge(vertex1, vertex2):
            self.update_edge_weight(vertex1, vertex2, weight)
            return
        # adding edge
        edge = [vertex2, weight, type]
        self.graph[vertex1].append(edge)
        # edge = [vertex1, weight, type]
        # self.graph[vertex2].append(edge)

    def find_shortest_path(self, starting_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[starting_vertex] = 0

        pq = [(0, starting_vertex)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue

            for edge in self.graph[current_vertex]:
                neighbor = edge[0]
                weight = edge[1]
                distance = current_distance + weight
                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def print_graph(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(vertex, "->", edge[0]," ( ", edge[1]," )")