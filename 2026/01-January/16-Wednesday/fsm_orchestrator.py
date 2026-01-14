import asyncio
import logging
from typing import Callable, Dict, List, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StateMachine:
    def __init__(self, initial_state: str):
        self.state = initial_state
        self.transitions: Dict[str, Dict[str, str]] = {}
        self.actions: Dict[str, List[Callable]] = {}
        self.history: List[Dict[str, Any]] = []

    def add_transition(self, from_state: str, event: str, to_state: str):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][event] = to_state

    def on_enter(self, state: str, action: Callable):
        if state not in self.actions:
            self.actions[state] = []
        self.actions[state].append(action)

    async def handle_event(self, event: str):
        if self.state in self.transitions and event in self.transitions[self.state]:
            old_state = self.state
            new_state = self.transitions[self.state][event]
            logging.info(f"Transitioning: {old_state} --({event})--> {new_state}")
            
            self.state = new_state
            self.history.append({\"from\": old_state, \"event\": event, \"to\": new_state})
            
            if new_state in self.actions:
                tasks = [asyncio.create_task(action()) for action in self.actions[new_state]]
                await asyncio.gather(*tasks)
        else:
            logging.warning(f"No transition found for event '{event}' in state '{self.state}'")

async def main():
    fsm = StateMachine(\"IDLE\")
    
    async def log_start():
        await asyncio.sleep(0.1)
        print(\"System started processing.\")

    async def log_finish():
        print(\"System reached completion state.\")

    fsm.add_transition(\"IDLE\", \"START\", \"RUNNING\")
    fsm.add_transition(\"RUNNING\", \"COMPLETE\", \"FINISHED\")
    
    fsm.on_enter(\"RUNNING\", log_start)
    fsm.on_enter(\"FINISHED\", log_finish)

    await fsm.handle_event(\"START\")
    await fsm.handle_event(\"COMPLETE\")

if __name__ == \"__main__\":
    asyncio.run(main())