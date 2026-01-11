import time

class TrafficLight:
    def __init__(self, initial_state="RED"):
        self.state = initial_state
        self.timer = 0
        self.state_durations = {
            "RED": 5,
            "GREEN": 5,
            "YELLOW": 2
        }

    def _transition(self):
        if self.state == "RED":
            self.state = "GREEN"
        elif self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"
        print(f"[{time.ctime()}] Traffic light transitioned to: {self.state}")
        self.timer = 0 # Reset timer on transition

    def update(self, delta_time):
        self.timer += delta_time
        if self.timer >= self.state_durations[self.state]:
            self._transition()

    def get_state(self):
        return self.state

def simulate_traffic_light(duration_seconds=15, step_interval=1):
    light = TrafficLight()
    print(f"[{time.ctime()}] Starting traffic light simulation. Initial state: {light.get_state()}")
    elapsed_time = 0
    while elapsed_time < duration_seconds:
        light.update(step_interval)
        time.sleep(step_interval)
        elapsed_time += step_interval
    print(f"[{time.ctime()}] Simulation ended.")

if __name__ == "__main__":
    simulate_traffic_light(duration_seconds=20, step_interval=1)