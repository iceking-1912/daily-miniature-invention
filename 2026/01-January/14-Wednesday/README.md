# State-Driven Workflow Engine

## Overview
This project implements a **Finite State Machine (FSM)** designed for document lifecycle management. In complex systems, managing the validity of state transitions is critical to prevent data corruption and illegal operations. This engine provides a deterministic way to move a document through its lifecycle.

## Technical Concepts
### 1. Finite State Machine (FSM)
The engine relies on a predefined set of states and transitions. By strictly enforcing that state changes only occur via defined events, we eliminate "impossible" states.

### 2. Type-Safe Transitions
Using TypeScript's union types (`State` and `Event`), the system ensures that only valid identifiers are used, providing compile-time safety alongside runtime validation.

### 3. Encapsulation
The internal state of the workflow is encapsulated within the `WorkflowEngine` class. The only way to modify the state is through the `transition` method, which acts as a gatekeeper.

## Why It Matters
As systems grow, logic for "what can happen when" often gets scattered across various services. Centralizing this logic into a state machine makes the system:
- **Testable:** Transitions are pure and predictable.
- **Maintainable:** Adding a new state or event requires updating a single transition table.
- **Robust:** It prevents logical errors, such as publishing a draft without approval.

## Usage
The engine is initialized at a 'DRAFT' state and can be moved through stages like 'REVIEW' and 'APPROVED' until it reaches its final 'ARCHIVED' state.
