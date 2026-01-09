import random

def create_initial_state(width: int) -> list[int]:
    """Generates an initial state for the cellular automaton, typically a single 'on' cell."""
    state = [0] * width
    state[width // 2] = 1 # Start with a single active cell in the middle
    return state

def get_neighborhood_value(left: int, center: int, right: int) -> int:
    """Calculates a 3-bit integer from the neighborhood state (e.g., 101 -> 5)."""
    return (left << 2) | (center << 1) | right

def apply_rule(current_state: list[int], rule_number: int) -> list[int]:
    """Applies a Wolfram cellular automaton rule to generate the next state.
    The rule_number (0-255) defines the behavior for each of the 8 possible 3-cell neighborhoods.
    """
    width = len(current_state)
    next_state = [0] * width
    
    # Pre-calculate the rule's output for each neighborhood pattern (0-7)
    rule_outputs = [(rule_number >> i) & 1 for i in range(8)]
    
    for i in range(width):
        left = current_state[(i - 1 + width) % width]  # Wrap around
        center = current_state[i]
        right = current_state[(i + 1) % width] # Wrap around
        
        neighborhood_index = get_neighborhood_value(left, center, right) # e.g., 101 -> 5
        next_state[i] = rule_outputs[neighborhood_index]
        
    return next_state

def simulate_automaton(initial_state: list[int], rule_number: int, generations: int) -> list[list[int]]:
    """Simulates the cellular automaton for a given number of generations,
    returning a history of all states.
    """
    history = [initial_state]
    current = initial_state
    
    for _ in range(generations - 1):
        current = apply_rule(current, rule_number)
        history.append(current)
        
    return history

def render_state(state: list[int], on_char: str = "█", off_char: str = " ") -> str:
    """Converts a state list (0s and 1s) into a printable string representation."""
    return "".join([on_char if cell == 1 else off_char for cell in state])

if __name__ == "__main__":
    WIDTH = 61 # Odd width for a symmetric initial state
    GENERATIONS = 30
    RULE = 30 # A famous rule known for producing complex, fractal-like patterns

    print(f"Simulating 1D Cellular Automaton (Rule {RULE})")
    print(f"Width: {WIDTH}, Generations: {GENERATIONS}\n")

    initial_cells = create_initial_state(WIDTH)
    
    evolution_history = simulate_automaton(initial_cells, RULE, GENERATIONS)
    
    for gen_num, state in enumerate(evolution_history):
        print(f"{gen_num:02d}: {render_state(state)}")
