import random

def initialize_grid(size: int, initial_pulse_pos: int) -> list[int]:
    """
    Initializes a 1D grid of cells with a single 'pulse' at a given position.
    Cell states are integers representing their 'energy' or 'intensity'.
    """
    if not (0 <= initial_pulse_pos < size):
        raise ValueError("Initial pulse position must be within grid bounds.")
    grid = [0] * size
    grid[initial_pulse_pos] = 5 # Starting pulse intensity
    return grid

def _calculate_next_state(current_val: int, left_val: int, right_val: int) -> int:
    """
    Applies a simple rule for cell evolution: a form of averaging and decay.
    The cell's next state is influenced by itself and its neighbors, then decays.
    """
    influence = (current_val * 2 + left_val + right_val) // 4
    decayed_influence = max(0, influence - 1) # Ensure state doesn't go below 0
    return decayed_influence

def evolve_system(grid: list[int], steps: int) -> list[list[int]]:
    """
    Evolves the 1D cellular system over a specified number of steps.
    Returns a list of grid states for each step, including the initial state.
    """
    history = [grid[:]] # Store initial state
    current_grid = grid[:]

    for _ in range(steps):
        next_grid = [0] * len(current_grid)
        size = len(current_grid)

        for i in range(size):
            left_neighbor = current_grid[(i - 1 + size) % size] # Toroidal boundary
            right_neighbor = current_grid[(i + 1) % size]      # Toroidal boundary
            next_grid[i] = _calculate_next_state(current_grid[i], left_neighbor, right_neighbor)

        current_grid = next_grid
        history.append(current_grid[:]) # Store the state after each step
    return history

def render_grid(grid_state: list[int]) -> str:
    """
    Renders a single grid state as a string, using intensity to represent characters.
    """
    # Using different characters for different intensity levels
    charset = " .:-=+*#%@"
    max_val = max(grid_state) if grid_state else 0
    # Scale values to fit within the charset, preventing division by zero
    scale_factor = (len(charset) - 1) / max(1, max_val)

    display_str = ""
    for val in grid_state:
        char_index = int(val * scale_factor)
        display_str += charset[min(char_index, len(charset) - 1)]
    return display_str

if __name__ == "__main__":
    GRID_SIZE = 40
    INITIAL_PULSE_POSITION = GRID_SIZE // 2
    EVOLUTION_STEPS = 30

    print(f"--- 1D Cellular Pulse Simulation (Size: {GRID_SIZE}, Steps: {EVOLUTION_STEPS}) ---")

    initial_state = initialize_grid(GRID_SIZE, INITIAL_PULSE_POSITION)
    print(f"Initial State: {render_grid(initial_state)}")

    evolution_history = evolve_system(initial_state, EVOLUTION_STEPS)

    print("\nEvolution History:")
    for step_num, state in enumerate(evolution_history):
        print(f"Step {step_num:02d}: {render_grid(state)}")

    print("\nSimulation complete.")
