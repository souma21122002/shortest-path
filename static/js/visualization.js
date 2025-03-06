let map;
let markers = {};
let currentPath = null;

const API_BASE_URL = window.location.origin;

async function initMap() {
    try {
        map = L.map('map').setView([20, 0], 2);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        
        await loadData();
    } catch (error) {
        console.error('Error initializing map:', error);
        alert('Error initializing map. Please check console for details.');
    }
}

async function loadData() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_graph_data`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        // Add markers and populate dropdowns
        Object.entries(data.vertices).forEach(([name, coords]) => {
            markers[name] = L.marker([coords[0], coords[1]])
                .bindPopup(name)
                .addTo(map);
                
            // Add to both dropdowns
            ['startPoint', 'endPoint'].forEach(id => {
                const option = document.createElement('option');
                option.value = name;
                option.textContent = name;
                document.getElementById(id).appendChild(option);
            });
        });
    } catch (error) {
        console.error('Error loading data:', error);
        alert('Error loading landmarks data. Please check console for details.');
    }
}

async function findShortestPath() {
    try {
        const start = document.getElementById('startPoint').value;
        const end = document.getElementById('endPoint').value;
        
        if (!start || !end) {
            alert('Please select both starting point and destination');
            return;
        }
        
        if (start === end) {
            alert('Starting point and destination must be different');
            return;
        }
        
        const response = await fetch(`${API_BASE_URL}/find_shortest_path`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ start, end })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to find path');
        }
        
        if (!data.path || !data.distance) {
            alert('No path found between selected landmarks');
            return;
        }
        
        displayPath(data.path, data.distance);
    } catch (error) {
        console.error('Error finding path:', error);
        alert('Error finding path: ' + error.message);
    }
}

function displayPath(path, distance) {
    // Clear previous path
    if (currentPath) {
        map.removeLayer(currentPath);
    }
    
    // Reset all markers to default
    Object.values(markers).forEach(marker => {
        marker.setIcon(new L.Icon.Default());
    });
    
    // Create path coordinates
    const pathCoords = path.map(name => {
        const [lat, lon] = markers[name].getLatLng();
        return [lat, lon];
    });
    
    // Draw new path
    currentPath = L.polyline(pathCoords, {
        color: 'red',
        weight: 3,
        opacity: 0.7
    }).addTo(map);
    
    // Update path details
    const pathDetails = document.getElementById('pathDetails');
    pathDetails.innerHTML = `
        <h3>Route Information</h3>
        <p><strong>Route:</strong> ${path.join(' → ')}</p>
        <p><strong>Total Distance:</strong> ${Math.round(distance).toLocaleString()} km</p>
        <p><strong>Estimated Travel Time:</strong> ${calculateTravelTime(distance)}</p>
    `;
    
    // Fit map to show entire path
    map.fitBounds(currentPath.getBounds(), { padding: [50, 50] });
}

// Add this helper function to calculate estimated travel time
function calculateTravelTime(distance) {
    // Assume average speed of 800 km/h for air travel
    const hours = distance / 800;
    if (hours < 1) {
        return `${Math.round(hours * 60)} minutes`;
    }
    const fullHours = Math.floor(hours);
    const minutes = Math.round((hours - fullHours) * 60);
    return `${fullHours} hour${fullHours !== 1 ? 's' : ''} ${minutes} minute${minutes !== 1 ? 's' : ''}`;
}

window.onload = initMap;