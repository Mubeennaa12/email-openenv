from tasks import load_task
from grader import compute_reward, check_done

class EmailEnv:

    def __init__(self):
        self.current_task = None
        self.state_data = None

    def reset(self, task_id):
        self.current_task = load_task(task_id)
        self.state_data = self.current_task["input"]
        return self.state_data

    def step(self, action):
        reward = compute_reward(action, self.current_task)
        done = check_done(action, self.current_task)
        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data