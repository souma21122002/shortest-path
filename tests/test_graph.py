import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.insert_vertex("A", 0, 0)
        self.graph.insert_vertex("B", 1, 1)
        self.graph.insert_edge("A", "B", 1.414)

    def test_insert_vertex(self):
        self.graph.insert_vertex("C", 2, 2)
        self.assertEqual(len(self.graph.vertex_list), 3)
        self.assertEqual(self.graph.vertex_list[-1].name, "C")

    def test_insert_edge(self):
        self.graph.insert_edge("A", "C", 2.828)
        self.assertEqual(self.graph.adj[self.graph.get_index("A")][self.graph.get_index("C")], 2.828)

    def test_dijkstra(self):
        paths = self.graph.find_paths("A")
        self.assertIn("B", paths)
        self.assertEqual(paths["B"], 1.414)

if __name__ == '__main__':
    unittest.main()