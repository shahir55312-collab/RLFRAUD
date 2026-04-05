RL Fraud Detection Environment

🚀 Overview

This project implements a Reinforcement Learning (RL) based environment for fraud detection.

🧠 Features

- Custom RL environment
- Q-learning agent
- FastAPI endpoints for interaction
- Dockerized deployment

📡 API Endpoints

- "GET /reset" → Reset environment
- "POST /step" → Take action

🐳 Run with Docker

docker build -t rl-fraud .
docker run -p 7860:7860 rl-fraud

⚙️ Run locally

uvicorn openenv.fast:app --reload

📁 Structure

- "model.py" → RL agent
- "fast.py" → FastAPI app
- "inference.py" → Evaluation script
- "openev.yaml" → Task config
