import time

class TrafficLight:
    def __init__(self, initial_state='red', red_duration=5, yellow_duration=2, green_duration=5):
        self.state = initial_state
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.last_transition_time = time.time()

    def _transition_state(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_transition_time

        if self.state == 'red' and elapsed_time >= self.red_duration:
            self.state = 'green'
            self.last_transition_time = current_time
        elif self.state == 'green' and elapsed_time >= self.green_duration:
            self.state = 'yellow'
            self.last_transition_time = current_time
        elif self.state == 'yellow' and elapsed_time >= self.yellow_duration:
            self.state = 'red'
            self.last_transition_time = current_time

    def get_current_state(self):
        self._transition_state()
        return self.state

    def simulate(self, duration_seconds):
        start_time = time.time()
        print(f"Simulating traffic light for {duration_seconds} seconds...")
        while (time.time() - start_time) < duration_seconds:
            print(f"Current state: {self.get_current_state()}")
            time.sleep(1) # Simulate checking state every second
        print("Simulation finished.")

if __name__ == "__main__":
    light = TrafficLight()
    light.simulate(15) # Simulate for 15 seconds
