# Event-Driven Industrial State Machine Simulation

## Overview
This project implements a robust finite-state machine (FSM) designed to simulate an industrial reactor's lifecycle. It explores the relationship between discrete state transitions and continuous telemetry updates.

## Key Technical Concepts
- **Deterministic State Transitions**: Using a transition table to manage valid system states (`IDLE`, `HEATING`, `PROCESSING`, etc.).
- **Telemetry Simulation**: Continuous integration of physical parameters (temperature, pressure) that influence or are influenced by the system state.
- **Event-Driven Architecture**: Decoupling the logic of *what* happens from *when* it happens by using triggered events.

## Why It Matters
In real-world industrial IoT (IIoT), systems must handle unpredictable sensor data while maintaining a strict operational sequence. This pattern provides a foundation for building safe, predictable control software for hardware systems where invalid state transitions could lead to physical damage.

## Lab Note
The simulation highlights the "HEATING" to "PROCESSING" transition threshold. In a production environment, this would likely be coupled with a PID controller for precision.
