type Grid = boolean[][];
type Particle = { x: number; y: number; };

const GRID_SIZE = 20;
const INITIAL_PARTICLES = 5;
const SIMULATION_STEPS = 100;

/**
 * Creates an initial grid with a central aggregated seed.
 * @param size The dimension of the square grid.
 * @returns A new Grid instance.
 */
function createInitialGrid(size: number): Grid {
    const grid: Grid = Array.from({ length: size }, () => Array(size).fill(false));
    const centerX = Math.floor(size / 2);
    const centerY = Math.floor(size / 2);
    grid[centerY][centerX] = true; // Central seed
    return grid;
}

/**
 * Generates a random position along the grid's edge for a new particle.
 * @param size The dimension of the square grid.
 * @returns A Particle object with x, y coordinates.
 */
function getRandomEdgePosition(size: number): Particle {
    const edge = Math.floor(Math.random() * 4); // 0:top, 1:right, 2:bottom, 3:left
    switch (edge) {
        case 0: return { x: Math.floor(Math.random() * size), y: 0 };
        case 1: return { x: size - 1, y: Math.floor(Math.random() * size) };
        case 2: return { x: Math.floor(Math.random() * size), y: size - 1 };
        case 3: return { x: 0, y: Math.floor(Math.random() * size) };
        default: return { x: 0, y: 0 }; // Should not happen
    }
}

/**
 * Moves a particle randomly to an adjacent cell, clamping within grid boundaries.
 * @param particle The particle to move.
 * @param size The dimension of the square grid.
 * @returns A new Particle object representing the new position.
 */
function moveParticle(particle: Particle, size: number): Particle {
    const dx = Math.floor(Math.random() * 3) - 1; // -1, 0, 1
    const dy = Math.floor(Math.random() * 3) - 1; // -1, 0, 1

    let newX = particle.x + dx;
    let newY = particle.y + dy;

    // Clamp to grid boundaries
    newX = Math.max(0, Math.min(size - 1, newX));
    newY = Math.max(0, Math.min(size - 1, newY));

    return { x: newX, y: newY };
}

/**
 * Checks if a given coordinate is adjacent to an aggregated cell in the grid.
 * @param x The x-coordinate to check.
 * @param y The y-coordinate to check.
 * @param grid The current grid state.
 * @param size The dimension of the square grid.
 * @returns True if adjacent to an aggregate, false otherwise.
 */
function isAdjacentToAggregate(x: number, y: number, grid: Grid, size: number): boolean {
    const neighbors = [
        { dx: -1, dy: 0 }, { dx: 1, dy: 0 },
        { dx: 0, dy: -1 }, { dx: 0, dy: 1 }
    ];

    for (const neighbor of neighbors) {
        const nx = x + neighbor.dx;
        const ny = y + neighbor.dy;

        if (nx >= 0 && nx < size && ny >= 0 && ny < size && grid[ny][nx]) {
            return true;
        }
    }
    return false;
}

/**
 * Simulates one step of the DLA process: moves particles and aggregates them if they touch the growing cluster.
 * @param grid The current state of the aggregation grid.
 * @param particles An array of current free-moving particles.
 * @param size The dimension of the square grid.
 * @returns An updated array of free-moving particles for the next step.
 */
function simulateDiffusionStep(grid: Grid, particles: Particle[], size: number): Particle[] {
    const nextParticles: Particle[] = [];
    const aggregatedCountThisStep = 0; // Track how many particles aggregated

    for (const particle of particles) {
        const newPos = moveParticle(particle, size);

        if (isAdjacentToAggregate(newPos.x, newPos.y, grid, size)) {
            // If the particle is adjacent to an aggregate, it sticks.
            // We also check if the cell itself isn't already part of the aggregate
            if (!grid[newPos.y][newPos.x]) {
                grid[newPos.y][newPos.x] = true; // Add to aggregate
                // aggregatedCountThisStep++; // Optionally track
            }
            // This particle has aggregated, so it's not added to `nextParticles`.
            // A new particle will be spawned to maintain density.
        } else {
            // If not aggregated, the particle continues moving.
            nextParticles.push(newPos);
        }
    }

    // Replenish particles that aggregated or were lost to maintain density
    while (nextParticles.length < INITIAL_PARTICLES) {
        nextParticles.push(getRandomEdgePosition(size));
    }

    return nextParticles;
}

/**
 * Renders the current grid state as a string using block characters.
 * @param grid The grid to render.
 * @returns A string representation of the grid.
 */
function renderGrid(grid: Grid): string {
    return grid.map(row =>
        row.map(cell => (cell ? '█' : ' ')).join('')
    ).join('
');
}

// --- Main Simulation Loop ---
let currentGrid: Grid = createInitialGrid(GRID_SIZE);
let currentParticles: Particle[] = Array.from({ length: INITIAL_PARTICLES }, () => getRandomEdgePosition(GRID_SIZE));

console.log("Initial State (Central Seed):");
console.log(renderGrid(currentGrid));
console.log("-".repeat(GRID_SIZE * 2)); // Separator

for (let i = 0; i < SIMULATION_STEPS; i++) {
    currentParticles = simulateDiffusionStep(currentGrid, currentParticles, GRID_SIZE);

    // Render the grid periodically to observe growth
    if ((i + 1) % 20 === 0 || i === SIMULATION_STEPS - 1) { // Render every 20 steps or at the end
        console.log(`
Simulation Step ${i + 1}:`);
        console.log(renderGrid(currentGrid));
        console.log("-".repeat(GRID_SIZE * 2));
    }
}

console.log("\nSimulation Complete.");
