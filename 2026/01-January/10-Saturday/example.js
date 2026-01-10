const GRID_SIZE = 10;
const INITIAL_CHARGE_DECAY_RATE = 0.05;
const PROPAGATION_FACTOR = 0.2;

/**
 * Initializes a square grid with random initial charge values.
 * @param {number} size - The side length of the square grid.
 * @returns {number[][]} A 2D array representing the grid state.
 */
function initializeGrid(size) {
    const grid = [];
    for (let i = 0; i < size; i++) {
        grid[i] = [];
        for (let j = 0; j < size; j++) {
            grid[i][j] = Math.random() * 10; // Initial charge between 0 and 10
        }
    }
    return grid;
}

/**
 * Calculates the net charge to apply to a specific cell for the next step.
 * This includes decay and propagation from neighbors.
 * @param {number[][]} currentGrid - The current state of the grid.
 * @param {number} row - The row index of the cell.
 * @param {number} col - The column index of the cell.
 * @returns {number} The new charge for the cell before clamping.
 */
function calculateNextCellCharge(currentGrid, row, col) {
    const size = currentGrid.length;
    let charge = currentGrid[row][col];

    // Apply decay to the current cell's charge
    charge -= charge * INITIAL_CHARGE_DECAY_RATE;

    // Accumulate propagated charge from direct neighbors (von Neumann neighborhood)
    const neighbors = [
        [row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]
    ];

    let propagatedCharge = 0;
    for (const [nRow, nCol] of neighbors) {
        if (nRow >= 0 && nRow < size && nCol >= 0 && nCol < size) {
            propagatedCharge += currentGrid[nRow][nCol] * PROPAGATION_FACTOR;
        }
    }

    return charge + propagatedCharge;
}

/**
 * Simulates one step of the energetic field evolution.
 * @param {number[][]} currentGrid - The current state of the grid.
 * @returns {number[][]} A new grid representing the state after one step.
 */
function simulateStep(currentGrid) {
    const size = currentGrid.length;
    const nextGrid = Array.from({ length: size }, () => Array(size).fill(0));

    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            let newCharge = calculateNextCellCharge(currentGrid, i, j);
            // Ensure charge stays non-negative and within a reasonable range
            nextGrid[i][j] = Math.max(0, Math.min(100, newCharge));
        }
    }
    return nextGrid;
}

/**
 * Displays the grid state, rounded for readability.
 * @param {number[][]} grid - The grid to display.
 * @param {number} step - The current simulation step.
 */
function displayGrid(grid, step) {
    console.log(`--- Step ${step} ---`);
    grid.forEach(row => {
        console.log(row.map(cell => cell.toFixed(2).padStart(6)).join(' '));
    });
}

// --- Main Simulation Loop ---
let grid = initializeGrid(GRID_SIZE);
const simulationSteps = 5;

console.log("Initial Grid:");
displayGrid(grid, 0);

for (let step = 1; step <= simulationSteps; step++) {
    grid = simulateStep(grid); // Update the grid state
    displayGrid(grid, step);
}
