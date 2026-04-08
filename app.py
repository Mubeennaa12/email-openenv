from fastapi import FastAPI
from env import EmailEnv

app = FastAPI()

env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset(1)
    return {"observation": obs}

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}
