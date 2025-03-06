# Shortest Path Project

## Overview
This project implements a graph data structure to find the shortest paths between vertices using Dijkstra's algorithm. It includes functionality to manage vertices and edges, as well as utilities for calculating distances based on geographical coordinates.

## Files
- `src/graph.py`: Contains the main logic for managing the graph.
- `src/models/vertex.py`: Defines the `Vertex` class representing a vertex in the graph.
- `src/utils/distance_calculator.py`: Utility functions for calculating distances between vertices.
- `src/main.py`: Entry point for the application.
- `tests/test_graph.py`: Unit tests for graph operations.
- `requirements.txt`: Lists project dependencies.

## Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd shortest-path
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Testing
To run the tests, use:
```
pytest tests/test_graph.py
```

## License
This project is licensed under the MIT License.