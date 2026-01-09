import random

GRID_SIZE = 10
MAX_VALUE = 9

def initialize_grid(size, max_val):
    """Creates a grid with random initial integer states."""
    grid = []
    for _ in range(size):
        row = [random.randint(0, max_val) for _ in range(size)]
        grid.append(row)
    return grid

def get_neighbors_sum(grid, r, c, size):
    """Calculates the sum of states of immediate cardinal neighbors."""
    total_neighbor_sum = 0
    neighbor_coords = [
        (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)
    ]
    for nr, nc in neighbor_coords:
        if 0 <= nr < size and 0 <= nc < size:
            total_neighbor_sum += grid[nr][nc]
    return total_neighbor_sum

def evolve_cell(current_state, neighbor_sum, max_val):
    """Applies a simple evolution rule to a cell's state."""
    # Rule: If sum of neighbors is even, increment state; if odd, decrement.
    # States wrap around 0 and max_val.
    if neighbor_sum % 2 == 0:
        new_state = (current_state + 1) % (max_val + 1)
    else:
        new_state = (current_state - 1 + (max_val + 1)) % (max_val + 1)
    return new_state

def simulate_evolution(initial_grid, generations, size, max_val):
    """Simulates the grid's evolution over multiple generations."""
    current_grid = [row[:] for row in initial_grid]
    
    history = [current_grid]

    for gen in range(generations):
        next_grid = [row[:] for row in current_grid]
        for r in range(size):
            for c in range(size):
                neighbor_sum = get_neighbors_sum(current_grid, r, c, size)
                next_grid[r][c] = evolve_cell(current_grid[r][c], neighbor_sum, max_val)
        current_grid = [row[:] for row in next_grid]
        history.append(current_grid)
    return history

def print_grid(grid, generation_num):
    """Prints the grid's current state."""
    print(f"\n--- Generation {generation_num} ---")
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    initial_grid = initialize_grid(GRID_SIZE, MAX_VALUE)
    
    print("Initial Grid:")
    print_grid(initial_grid, 0)
    
    simulation_generations = 5
    evolution_history = simulate_evolution(initial_grid, simulation_generations, GRID_SIZE, MAX_VALUE)
    
    for i, grid_state in enumerate(evolution_history[1:]):
        print_grid(grid_state, i + 1)
