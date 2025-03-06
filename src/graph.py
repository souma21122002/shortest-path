from math import radians, sin, cos, sqrt, atan2
import heapq

class Graph:
    def __init__(self):
        """Initialize an empty graph"""
        self.vertices = {}  # Dictionary to store vertices with their coordinates
        self.edges = []  # List to store edges
        self.distances = {}  # Dictionary to store distances between vertices

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        """Calculate distance between two points using Haversine formula"""
        R = 6371  # Earth's radius in km
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return R * c

    def insert_vertex(self, name, lat, lon):
        """Insert a vertex with name and coordinates"""
        self.vertices[name] = (lat, lon)

    def insert_edge(self, from_vertex, to_vertex):
        """Insert an edge and calculate its distance"""
        if from_vertex in self.vertices and to_vertex in self.vertices:
            lat1, lon1 = self.vertices[from_vertex]
            lat2, lon2 = self.vertices[to_vertex]
            distance = self.calculate_distance(lat1, lon1, lat2, lon2)
            
            self.edges.append((from_vertex, to_vertex))
            self.distances[(from_vertex, to_vertex)] = distance
            self.distances[(to_vertex, from_vertex)] = distance  # Bidirectional

    def get_neighbors(self, vertex):
        """Get all neighboring vertices of a given vertex"""
        if vertex not in self.vertices:
            return []

        neighbors = []
        for edge in self.edges:
            if edge[0] == vertex:
                neighbors.append(edge[1])
            elif edge[1] == vertex:
                neighbors.append(edge[0])
        return neighbors

    def find_shortest_path(self, start, end):
        """
        Find shortest path between start and end vertices using Dijkstra's algorithm
        Returns:
            tuple: (path, total_distance) or (None, None) if no path exists
        """
        if start not in self.vertices or end not in self.vertices:
            return None, None

        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]
        previous = {vertex: None for vertex in self.vertices}

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == end:
                break

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.get_neighbors(current_vertex):
                if (current_vertex, neighbor) not in self.distances:
                    continue
                
                new_distance = current_distance + self.distances[(current_vertex, neighbor)]
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))

        if distances[end] == float('infinity'):
            return None, None

        # Reconstruct path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path, distances[end]

    def find_paths(self, start):
        """Find all possible paths from start vertex using DFS"""
        if start not in self.vertices:
            return []

        visited = set()
        all_paths = []

        def dfs(current, path, total_distance=0):
            visited.add(current)
            path.append(current)
            
            all_paths.append((path[:], total_distance))
            
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    distance = self.distances.get((current, neighbor), 0)
                    dfs(neighbor, path[:], total_distance + distance)
            
            visited.remove(current)

        dfs(start, [], 0)
        return all_paths
