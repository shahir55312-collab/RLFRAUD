from fastapi import FastAPI
from openenv.model import AMLauditor

app = FastAPI()
env = AMLauditor()

@app.get("/reset")
def reset():
    state, _ = env.reset()
    return {"state": state.tolist()}

@app.post("/step")
def step(action: int):
    state, reward, terminated, _ = env.step(action)
    return {
        "state": state.tolist(),
        "reward": reward,
        "terminated": terminated
    }