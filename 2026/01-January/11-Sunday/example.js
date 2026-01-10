/**
 * Represents a single node in the FluxField simulation.
 * Each node holds a certain amount of 'flux' (resource) and has a maximum capacity.
 */
class FluxNode {
    constructor(id, initialFlux, capacity, neighbors = []) {
        this.id = id;
        this.flux = initialFlux;
        this.capacity = capacity;
        this.neighbors = new Set(neighbors); // Use Set for efficient neighbor management
    }

    // Adds a neighbor to this node
    addNeighbor(nodeId) {
        this.neighbors.add(nodeId);
    }

    // Removes a neighbor from this node
    removeNeighbor(nodeId) {
        this.neighbors.delete(nodeId);
    }
}

/**
 * Simulates the flow of 'flux' between interconnected nodes over discrete ticks.
 * The simulation aims to balance flux among neighboring nodes.
 */
class FluxField {
    constructor(nodeConfigs) {
        this.nodes = new Map(); // Store nodes by ID for quick access
        nodeConfigs.forEach(config => {
            const node = new FluxNode(config.id, config.initialFlux, config.capacity);
            this.nodes.set(node.id, node);
        });

        // Establish neighbors after all nodes are created
        nodeConfigs.forEach(config => {
            const node = this.nodes.get(config.id);
            if (config.neighbors) {
                config.neighbors.forEach(neighborId => {
                    if (this.nodes.has(neighborId)) {
                        node.addNeighbor(neighborId);
                        this.nodes.get(neighborId).addNeighbor(node.id); // Bidirectional connection
                    }
                });
            }
        });
    }

    /**
     * Executes one simulation tick, allowing flux to transfer between nodes.
     * Flux transfer logic: Neighbors try to equalize their flux, limited by capacity.
     */
    simulateTick(transferRate = 0.1) {
        const fluxChanges = new Map(); // Store pending changes to apply at the end of the tick

        // Initialize all nodes with zero change for this tick
        this.nodes.forEach(node => fluxChanges.set(node.id, 0));

        // Calculate potential transfers
        this.nodes.forEach(node => {
            node.neighbors.forEach(neighborId => {
                const neighbor = this.nodes.get(neighborId);
                if (!neighbor || node.id >= neighbor.id) return; // Process each pair once to avoid double counting

                const fluxDifference = node.flux - neighbor.flux;
                const availableToTransfer = Math.min(
                    Math.abs(fluxDifference) * transferRate,
                    Math.max(0, node.flux), // Cannot transfer more than current flux
                    Math.max(0, neighbor.capacity - neighbor.flux) // Cannot transfer more than neighbor's remaining capacity
                );

                if (fluxDifference > 0) { // Node has more flux than neighbor
                    fluxChanges.set(node.id, fluxChanges.get(node.id) - availableToTransfer);
                    fluxChanges.set(neighbor.id, fluxChanges.get(neighbor.id) + availableToTransfer);
                } else if (fluxDifference < 0) { // Neighbor has more flux than node
                    fluxChanges.set(neighbor.id, fluxChanges.get(neighbor.id) - availableToTransfer);
                    fluxChanges.set(node.id, fluxChanges.get(node.id) + availableToTransfer);
                }
            });
        });

        // Apply calculated changes
        this.nodes.forEach(node => {
            const change = fluxChanges.get(node.id);
            if (change !== undefined) {
                node.flux += change;
                // Ensure flux stays within bounds [0, capacity]
                node.flux = Math.max(0, Math.min(node.flux, node.capacity));
            }
        });
    }

    // Returns a snapshot of the current state of all nodes
    getState() {
        const state = {};
        this.nodes.forEach(node => {
            state[node.id] = { flux: parseFloat(node.flux.toFixed(2)), capacity: node.capacity };
        });
        return state;
    }
}

// --- Simulation Setup and Execution ---
if (typeof module !== 'undefined' && module.exports) {
    // Export for testing or module usage in Node.js
    module.exports = { FluxNode, FluxField };
} else {
    // Direct execution in browser or Node.js environment
    const nodeConfigurations = [
        { id: 'A', initialFlux: 100, capacity: 150, neighbors: ['B', 'C'] },
        { id: 'B', initialFlux: 50, capacity: 100, neighbors: ['A', 'D'] },
        { id: 'C', initialFlux: 120, capacity: 150, neighbors: ['A', 'D'] },
        { id: 'D', initialFlux: 30, capacity: 80, neighbors: ['B', 'C'] },
        { id: 'E', initialFlux: 70, capacity: 100, neighbors: ['F'] }, // Isolated path
        { id: 'F', initialFlux: 10, capacity: 100, neighbors: ['E'] }
    ];

    const field = new FluxField(nodeConfigurations);

    console.log("Initial State:");
    console.log(field.getState());

    const totalTicks = 20;
    for (let i = 0; i < totalTicks; i++) {
        field.simulateTick(0.15); // Adjust transfer rate
        if ((i + 1) % 5 === 0 || i === totalTicks - 1) { // Log state every 5 ticks or at the end
            console.log(`\nState after Tick ${i + 1}:`);
            console.log(field.getState());
        }
    }
}
