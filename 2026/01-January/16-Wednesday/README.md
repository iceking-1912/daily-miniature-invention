# Async State Machine Orchestrator

This project implements a self-contained Asynchronous Finite State Machine (FSM) in Python. It explores the intersection of state-based logic and event-driven programming.

### Key Technical Ideas
- **Asynchronous Execution**: Using `asyncio` to handle state entry actions allows for non-blocking side effects when transitions occur.
- **Transition Mapping**: A flexible dictionary-based structure for defining valid state hops.
- **History Tracking**: Each transition is recorded, providing a deterministic audit trail of the system's behavior.

### Why It Matters
Complex systems often suffer from \"spaghetti logic\" when managing state. A formal state machine provides a declarative way to manage transitions, making code easier to reason about, test, and debug.
