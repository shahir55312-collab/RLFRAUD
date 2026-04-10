import requests

BASE_URL = "http://127.0.0.1:7860"


res = requests.get(f"{BASE_URL}/reset")
data = res.json()
state = data["state"]

print("Initial State:", state)


action = 1  

res = requests.post(f"{BASE_URL}/step", params={"action": action})
result = res.json()

print("Action:", action)
print("Next State:", result["state"])
print("Reward:", result["reward"])
print("Done:", result["done"])
