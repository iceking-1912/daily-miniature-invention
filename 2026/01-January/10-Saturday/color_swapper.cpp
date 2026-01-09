#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <chrono> // For seeding

// Define grid dimensions
const int GRID_WIDTH = 20;
const int GRID_HEIGHT = 10;
const int NUM_COLORS = 3; // 'R', 'G', 'B'

// Function to initialize the grid with random colors
void initializeGrid(std::vector<std::vector<char>>& grid, std::mt19937& rng) {
    std::uniform_int_distribution<int> dist(0, NUM_COLORS - 1);
    char colors[] = {'R', 'G', 'B'};
    for (int i = 0; i < GRID_HEIGHT; ++i) {
        for (int j = 0; j < GRID_WIDTH; ++j) {
            grid[i][j] = colors[dist(rng)];
        }
    }
}

// Function to print the grid
void printGrid(const std::vector<std::vector<char>>& grid) {
    for (int i = 0; i < GRID_HEIGHT; ++i) {
        for (int j = 0; j < GRID_WIDTH; ++j) {
            std::cout << grid[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

// Function to evolve the grid state based on neighbor interaction
void evolveGrid(std::vector<std::vector<char>>& currentGrid, std::mt19937& rng) {
    std::vector<std::vector<char>> nextGrid = currentGrid; // Create a buffer for next state
    std::uniform_real_distribution<double> chance_dist(0.0, 1.0);
    const double SWAP_CHANCE = 0.2; // 20% chance to adopt neighbor's color

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1}; // Neighbor row offsets (8 directions)
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1}; // Neighbor col offsets (8 directions)

    for (int i = 0; i < GRID_HEIGHT; ++i) {
        for (int j = 0; j < GRID_WIDTH; ++j) {
            // Pick a random neighbor direction for the current cell to consider
            int neighbor_idx = std::uniform_int_distribution<int>(0, 7)(rng); 
            int ni = i + dr[neighbor_idx];
            int nj = j + dc[neighbor_idx];

            // Check boundaries for the chosen neighbor
            if (ni >= 0 && ni < GRID_HEIGHT && nj >= 0 && nj < GRID_WIDTH) {
                // If the current cell's color is different from the neighbor's color
                if (currentGrid[i][j] != currentGrid[ni][nj]) {
                    // With a certain probability, adopt the neighbor's color
                    if (chance_dist(rng) < SWAP_CHANCE) {
                        nextGrid[i][j] = currentGrid[ni][nj]; 
                    }
                }
            }
        }
    }
    currentGrid = nextGrid; // Update the grid to the next state
}

int main() {
    // Seed random number generator using current time
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::mt19937 rng(seed);

    // Initialize the grid with specified dimensions
    std::vector<std::vector<char>> grid(GRID_HEIGHT, std::vector<char>(GRID_WIDTH));

    initializeGrid(grid, rng);
    std::cout << "Initial State:" << std::endl;
    printGrid(grid);

    const int EVOLUTION_STEPS = 10; // Number of simulation steps
    for (int step = 0; step < EVOLUTION_STEPS; ++step) {
        evolveGrid(grid, rng);
        std::cout << "State after step " << step + 1 << ":" << std::endl;
        printGrid(grid);
    }

    return 0;
}
