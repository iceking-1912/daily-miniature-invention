// trafficLight.js

/**
 * Represents a simple traffic light state machine.
 */
class TrafficLight {
    constructor() {
        this.states = {
            red: { next: 'green', duration: 5000 },
            green: { next: 'yellow', duration: 4000 },
            yellow: { next: 'red', duration: 2000 }
        };
        this.currentState = 'red';
        this.timer = null;
        console.log(`Traffic light initialized to: ${this.currentState}`);
    }

    /**
     * Transitions the traffic light to the next state.
     */
    transition() {
        const nextState = this.states[this.currentState].next;
        this.currentState = nextState;
        console.log(`Traffic light changed to: ${this.currentState}`);
        this.startTimer();
    }

    /**
     * Starts a timer for the current state's duration.
     */
    startTimer() {
        if (this.timer) {
            clearTimeout(this.timer);
        }
        const duration = this.states[this.currentState].duration;
        this.timer = setTimeout(() => this.transition(), duration);
    }

    /**
     * Starts the traffic light simulation.
     */
    start() {
        console.log('Traffic light simulation started.');
        this.startTimer();
    }

    /**
     * Stops the traffic light simulation.
     */
    stop() {
        if (this.timer) {
            clearTimeout(this.timer);
            this.timer = null;
        }
        console.log('Traffic light simulation stopped.');
    }

    /**
     * Gets the current state of the traffic light.
     * @returns {string} The current state.
     */
    getState() {
        return this.currentState;
    }
}

// Example Usage:
// const light = new TrafficLight();
// light.start();
// // To stop after some time:
// // setTimeout(() => light.stop(), 20000);