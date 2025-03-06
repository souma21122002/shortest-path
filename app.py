from flask import Flask, render_template, jsonify, request
from src.graph import Graph

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_graph_data')
def get_graph_data():
    graph = Graph()

    # Add landmarks with their coordinates
    graph.insert_vertex("Eiffel Tower", 48.8584, 2.2945)
    graph.insert_vertex("Colosseum", 41.8902, 12.4922)
    graph.insert_vertex("Statue of Liberty", 40.6892, -74.0445)
    graph.insert_vertex("Machu Picchu", -13.1631, -72.5450)
    graph.insert_vertex("Acropolis", 37.9715, 23.7257)
    graph.insert_vertex("Taj Mahal", 27.1751, 78.0421)
    graph.insert_vertex("Pyramids of Giza", 29.9792, 31.1342)
    graph.insert_vertex("Great Wall of China", 40.4319, 116.5704)
    graph.insert_vertex("Angkor Wat", 13.4125, 103.8670)
    graph.insert_vertex("Petra", 30.3285, 35.4444)

    # Add connections between landmarks
    graph.insert_edge("Eiffel Tower", "Colosseum")
    graph.insert_edge("Eiffel Tower", "Statue of Liberty")
    graph.insert_edge("Colosseum", "Acropolis")
    graph.insert_edge("Statue of Liberty", "Machu Picchu")
    graph.insert_edge("Machu Picchu", "Taj Mahal")
    graph.insert_edge("Acropolis", "Pyramids of Giza")
    graph.insert_edge("Taj Mahal", "Great Wall of China")
    graph.insert_edge("Pyramids of Giza", "Petra")
    graph.insert_edge("Great Wall of China", "Angkor Wat")
    graph.insert_edge("Angkor Wat", "Petra")

    return jsonify({
        'vertices': graph.vertices,
        'edges': graph.edges
    })


@app.route('/find_paths/<start>')
def find_paths_route(start):
    graph = Graph()
    # Recreate the graph as above
    # Add vertices and edges...
    paths = []

    def path_callback(path):
        paths.append(path[:])

    graph.find_paths(start)
    return jsonify({'paths': paths})


@app.route('/find_shortest_path', methods=['POST'])
def find_shortest_path_route():
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')

    if not start or not end:
        return jsonify({'error': 'Start and end points are required'}), 400

    graph = Graph()

    # Add landmarks with their coordinates
    graph.insert_vertex("Eiffel Tower", 48.8584, 2.2945)
    graph.insert_vertex("Colosseum", 41.8902, 12.4922)
    graph.insert_vertex("Statue of Liberty", 40.6892, -74.0445)
    graph.insert_vertex("Machu Picchu", -13.1631, -72.5450)
    graph.insert_vertex("Acropolis", 37.9715, 23.7257)
    graph.insert_vertex("Taj Mahal", 27.1751, 78.0421)
    graph.insert_vertex("Pyramids of Giza", 29.9792, 31.1342)
    graph.insert_vertex("Great Wall of China", 40.4319, 116.5704)
    graph.insert_vertex("Angkor Wat", 13.4125, 103.8670)
    graph.insert_vertex("Petra", 30.3285, 35.4444)

    # Add connections between landmarks
    graph.insert_edge("Eiffel Tower", "Colosseum")
    graph.insert_edge("Eiffel Tower", "Statue of Liberty")
    graph.insert_edge("Colosseum", "Acropolis")
    graph.insert_edge("Statue of Liberty", "Machu Picchu")
    graph.insert_edge("Machu Picchu", "Taj Mahal")
    graph.insert_edge("Acropolis", "Pyramids of Giza")
    graph.insert_edge("Taj Mahal", "Great Wall of China")
    graph.insert_edge("Pyramids of Giza", "Petra")
    graph.insert_edge("Great Wall of China", "Angkor Wat")
    graph.insert_edge("Angkor Wat", "Petra")

    path, distance = graph.find_shortest_path(start, end)
    
    if path is None:
        return jsonify({'error': 'No path found between the specified landmarks'}), 404

    return jsonify({
        'path': path,
        'distance': distance
    })


if __name__ == '__main__':
    app.run(debug=True)