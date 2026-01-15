# Reactive Dependency Graph

A minimalist implementation of a reactive programming model using a dependency graph in Python.

### Key Technical Ideas
- **Lazy Evaluation**: Values are only recomputed when requested, minimizing overhead.
- **Dirty Propagation**: Changes in leaf nodes mark dependent nodes as "dirty" rather than recalculating the entire graph immediately.
- **Memoization**: Computed values are stored (cached) until dependencies change.
- **Directed Acyclic Graph (DAG)**: The system naturally forms a DAG where nodes represent state or computations.

### Why it Matters
This pattern is the foundation of modern UI frameworks and build systems. Understanding how state changes propagate through a system is crucial for optimizing performance in complex, state-heavy applications. By decoupling state updates from re-evaluations, we can create more efficient and predictable systems.
