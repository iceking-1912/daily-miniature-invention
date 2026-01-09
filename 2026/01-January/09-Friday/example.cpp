#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

// Function to initialize the energy chain with a source
std::vector<int> initializeChain(int size, int initialEnergyAtSource) {
    std::vector<int> chain(size, 0);
    if (size > 0) {
        chain[0] = initialEnergyAtSource; // The initial energy for the source cell
    }
    return chain;
}

// Function to evolve the energy chain for one step
void evolveChain(std::vector<int>& chain) {
    if (chain.empty()) return;

    std::vector<int> nextChain = chain; // Start with a copy of the current state

    // Define constants for evolution rules
    const int sourceEnergyGain = 5;
    const int dissipationPerCell = 1;
    const int propagationAmount = 1;
    const int minEnergyToPropagate = 3; // Must have at least this much to propagate 1 unit

    // Special rule for the source cell (index 0):
    // It first gains energy, then behaves like others for dissipation and propagation.
    nextChain[0] += sourceEnergyGain; // Source consistently generates energy

    // Iterate through all cells to apply rules
    // Rules depend on the *original* state (`chain`) for propagation decisions
    // and update the *next* state (`nextChain`).
    for (int i = 0; i < chain.size(); ++i) {
        // 1. Dissipation: Every cell loses some energy
        nextChain[i] = std::max(0, nextChain[i] - dissipationPerCell);

        // 2. Propagation: Energy moves to the right
        // This depends on the *original* energy of the current cell (`chain[i]`)
        // to decide if propagation occurs.
        if (chain[i] >= minEnergyToPropagate && i + 1 < chain.size()) {
            nextChain[i] -= propagationAmount;   // Current cell loses energy
            nextChain[i+1] += propagationAmount; // Next cell gains energy
        }

        // Ensure no cell's energy drops below zero due to any operation
        nextChain[i] = std::max(0, nextChain[i]);
    }
    // After the loop, the nextChain is fully computed. Update the actual chain.
    chain = nextChain;
}

// Function to print the current state of the chain
void printChain(const std::vector<int>& chain, int step) {
    std::cout << "Step " << step << ": [";
    for (size_t i = 0; i < chain.size(); ++i) {
        std::cout << chain[i];
        if (i < chain.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

int main() {
    const int chainSize = 8; // A small chain to easily observe propagation
    const int initialSourceEnergy = 10;
    const int totalSimulationSteps = 15; // Run for enough steps to see patterns emerge

    std::vector<int> energyChain = initializeChain(chainSize, initialSourceEnergy);

    // Simulate and print the chain's state at each step
    for (int step = 0; step <= totalSimulationSteps; ++step) {
        printChain(energyChain, step);
        evolveChain(energyChain);
    }

    return 0;
}
