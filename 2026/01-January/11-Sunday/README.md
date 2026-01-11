# Traffic Light State Machine Simulation

## Overview

This project implements a basic simulation of a traffic light using a state machine pattern in JavaScript. It demonstrates how to manage sequential states with predefined transitions and durations, a common requirement in embedded systems, UI components, and process automation.

## Key Technical Concepts

1.  **State Machine:** The core of this simulation. A state machine is a mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The state machine can change from one state to another in response to some external inputs; the change from one state to another is called a transition.
2.  **States:** The traffic light has three distinct states: `red`, `green`, and `yellow`. Each state is defined with its next sequential state and a duration for which the light remains in that state.
3.  **Transitions:** The movement between states (e.g., `red` to `green`, `green` to `yellow`, `yellow` to `red`) is handled by the `transition` method, which updates the `currentState` property.
4.  **Timers (Asynchronous Operations):** JavaScript's `setTimeout` function is used to control the duration each light stays on. This introduces an asynchronous element, mimicking real-world timing mechanisms. `clearTimeout` is used to manage the timer, ensuring only one timer is active at a time.
5.  **Encapsulation:** The `TrafficLight` class encapsulates the states, current state, and methods for state transitions and timer management, providing a clean interface for interaction.

## Why it Matters (Engineer's Lab Note)

Understanding and implementing state machines is fundamental in various engineering disciplines. For front-end development, they can manage complex UI component states (e.g., form submissions, modal windows). In backend systems, they are crucial for workflow management (e.g., order processing, build pipelines). In embedded systems, they are ubiquitous for controlling hardware.

This particular implementation highlights:
*   **Predictable Behavior:** By defining explicit states and transitions, the system's behavior becomes predictable and easier to debug.
*   **Modularity:** Each state's logic and transitions are clearly defined, making it easy to add new states or modify existing ones without affecting unrelated parts of the system.
*   **Event-Driven Design:** The state changes are driven by the completion of a timer event, a common pattern in event-driven architectures.

This simple traffic light example serves as a foundational building block for more complex state-driven systems, emphasizing clarity, control, and maintainability.