class Vertex:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.status = 1  # TEMPORARY
        self.predecessor = -1  # NIL
        self.path_length = float('inf')  # INT_INFINITY
        self.latitude = latitude
        self.longitude = longitude