/**
 * Represents the state of a single cell in the 1D cellular automaton.
 * 0 usually represents 'dead' or 'off', 1 represents 'alive' or 'on'.
 */
type CellState = 0 | 1;

/**
 * Implements Wolfram's Rule 30 for a 1D cellular automaton.
 * The rule determines the next state of the center cell based on its
 * current state and the states of its immediate left and right neighbors.
 *
 * Rule 30 truth table (left, center, right -> new_center):
 * 111 -> 0
 * 110 -> 0
 * 101 -> 0
 * 100 -> 1
 * 011 -> 1
 * 010 -> 1
 * 001 -> 1
 * 000 -> 0
 */
function getRule30NextState(left: CellState, center: CellState, right: CellState): CellState {
    if (left === 1 && center === 1 && right === 1) return 0;
    if (left === 1 && center === 1 && right === 0) return 0;
    if (left === 1 && center === 0 && right === 1) return 0;
    if (left === 1 && center === 0 && right === 0) return 1;
    if (left === 0 && center === 1 && right === 1) return 1;
    if (left === 0 && center === 1 && right === 0) return 1;
    if (left === 0 && center === 0 && right === 1) return 1;
    if (left === 0 && center === 0 && right === 0) return 0;
    return 0; // Fallback, though inputs should be strictly 0 or 1
}

/**
 * Evolves the 1D cellular automaton by one generation using Rule 30.
 *
 * @param currentState An array representing the current state of the cells.
 * @returns A new array representing the next state of the cells.
 */
function evolve(currentState: CellState[]): CellState[] {
    const nextState: CellState[] = new Array(currentState.length).fill(0);
    const width = currentState.length;

    for (let i = 0; i < width; i++) {
        // Handle boundary conditions: assume cells outside the world are '0'.
        const left = i === 0 ? 0 : currentState[i - 1];
        const center = currentState[i];
        const right = i === width - 1 ? 0 : currentState[i + 1];

        nextState[i] = getRule30NextState(left, center, right);
    }

    return nextState;
}

/**
 * Renders the cellular automaton state as a string, using characters
 * to represent 'on' and 'off' cells.
 * @param state The current state of the cells.
 * @returns A string representation of the state.
 */
function renderState(state: CellState[]): string {
    return state.map(cell => (cell === 1 ? '█' : ' ')).join('');
}

// --- Main Simulation --- 
const INITIAL_WIDTH = 61; // Must be an odd number for a single center seed
const GENERATIONS = 30;

// Initialize the world with a single 'on' cell in the center
let currentWorld: CellState[] = new Array(INITIAL_WIDTH).fill(0);
currentWorld[Math.floor(INITIAL_WIDTH / 2)] = 1;

console.log("1D Cellular Automaton: Rule 30 Simulation");
console.log("Initial state:");
console.log(renderState(currentWorld));

for (let gen = 0; gen < GENERATIONS; gen++) {
    currentWorld = evolve(currentWorld);
    console.log(`Generation ${String(gen + 1).padStart(2, '0')}: ${renderState(currentWorld)}`);
}
