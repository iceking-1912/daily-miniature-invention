import random

RESET = "\033[0m"
BLUE = "\033[34m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
DARK_GREEN = "\033[92m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def random_grid(w, h, seed=None):
    if seed is not None:
        random.seed(seed)
    return [[random.random() for _ in range(w)] for _ in range(h)]

def smooth(grid, it=1):
    h, w = len(grid), len(grid[0])
    pad = [[0]*(w+2) for _ in range(h+2)]
    for y in range(h):
        for x in range(w):
            pad[y+1][x+1] = grid[y][x]

    for _ in range(it):
        new = [[0]*w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                s = 0
                for dy in (-1,0,1):
                    for dx in (-1,0,1):
                        s += pad[y+1+dy][x+1+dx]
                new[y][x] = s / 9

        for y in range(h):
            for x in range(w):
                pad[y+1][x+1] = new[y][x]

    return new

def normalize(grid):
    flat = [v for r in grid for v in r]
    mn, mx = min(flat), max(flat)
    return [[(v-mn)/(mx-mn) for v in row] for row in grid]

def fractal_noise(w, h, seed, layers=4):
    noise = [[0]*w for _ in range(h)]
    amp = 1
    total = 0

    for i in range(layers):
        g = random_grid(w, h, seed+i)
        g = smooth(g, 4 + i*2)
        for y in range(h):
            for x in range(w):
                noise[y][x] += g[y][x] * amp
        total += amp
        amp *= 0.5

    for y in range(h):
        for x in range(w):
            noise[y][x] /= total

    return normalize(noise)

def generate_map(w, h, seed):
    print("Seed:", seed)

    elev = fractal_noise(w, h, seed)
    hum  = fractal_noise(w, h, seed+999)

    world = [["" for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            e = elev[y][x]
            hmd = hum[y][x]

            # 🌊 Water
            if e < 0.35:
                world[y][x] = BLUE + "🌊" + RESET
            elif e < 0.42:
                world[y][x] = CYAN + "💧" + RESET

            # 🏔️ Land
            else:
                if e > 0.85:
                    world[y][x] = WHITE + "❄️" + RESET        # Snow
                elif e > 0.70:
                    world[y][x] = GRAY + "⛰️" + RESET        # Mountain
                else:
                    if hmd < 0.30:
                        world[y][x] = YELLOW + "🏜️" + RESET  # Desert
                    elif hmd < 0.50:
                        world[y][x] = GREEN + "🌾" + RESET   # Grassland
                    elif hmd < 0.75:
                        world[y][x] = DARK_GREEN + "🌲" + RESET # Forest
                    else:
                        world[y][x] = DARK_GREEN + "🌳" + RESET # Dense Forest

    return world

def display(world):
    for row in world:
        print("".join(row))

# ==== MAIN ====
if __name__ == "__main__":
    WIDTH = 50
    HEIGHT = 25
    SEED = 23798324230894329508934573940503487503475934750
    

    planet = generate_map(WIDTH, HEIGHT, SEED)
    print()
    display(planet)

    print("\nLegend:")
    print(BLUE + "🌊" + RESET, "Deep Water")
    print(CYAN + "💧" + RESET, "Shallow Water")
    print(YELLOW + "🏜️" + RESET, "Desert")
    print(GREEN + "🌾" + RESET, "Grassland")
    print(DARK_GREEN + "🌲" + RESET, "Forest")
    print(DARK_GREEN + "🌳" + RESET, "Dense Forest")
    print(GRAY + "⛰️" + RESET, "Mountain")
    print(WHITE + "❄️" + RESET, "Snow Peak")
