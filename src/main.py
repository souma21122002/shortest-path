from graph import Graph

def main():
    graph = Graph()

    # Insert vertices with their names and coordinates
    graph.insert_vertex("Eiffel Tower", 48.8584, 2.2945)  # Paris
    graph.insert_vertex("Colosseum", 41.8902, 12.4922)  # Rome
    graph.insert_vertex("Statue of Liberty", 40.6892, -74.0445)  # New York
    graph.insert_vertex("Machu Picchu", -13.1631, -72.5450)  # Peru
    graph.insert_vertex("Acropolis", 37.9715, 23.7257)  # Athens
    graph.insert_vertex("Taj Mahal", 27.1751, 78.0421)  # India
    graph.insert_vertex("Pyramids of Giza", 29.9792, 31.1342)  # Egypt
    graph.insert_vertex("Great Wall of China", 40.4319, 116.5704)  # China
    graph.insert_vertex("Angkor Wat", 13.4125, 103.8670)  # Cambodia
    graph.insert_vertex("Petra", 30.3285, 35.4444)  # Jordan

    # Insert edges based on hypothetical distances
    graph.insert_edge("Eiffel Tower", "Colosseum")  # Distance placeholder
    graph.insert_edge("Eiffel Tower", "Statue of Liberty")  # Distance placeholder
    graph.insert_edge("Colosseum", "Acropolis")  # Distance placeholder
    graph.insert_edge("Statue of Liberty", "Machu Picchu")  # Distance placeholder
    graph.insert_edge("Machu Picchu", "Taj Mahal")  # Distance placeholder
    graph.insert_edge("Acropolis", "Pyramids of Giza")  # Distance placeholder
    graph.insert_edge("Taj Mahal", "Great Wall of China")  # Distance placeholder
    graph.insert_edge("Pyramids of Giza", "Petra")  # Distance placeholder
    graph.insert_edge("Great Wall of China", "Angkor Wat")  # Distance placeholder
    graph.insert_edge("Angkor Wat", "Petra")  # Distance placeholder

    # Assuming "Eiffel Tower" is the starting point
    graph.find_paths("Eiffel Tower")

if __name__ == "__main__":
    main()