def main():
    task_name = "rl-agent"

    # START block
    print(f"[START] task={task_name}", flush=True)

    total_reward = 0
    steps = 0

    # simulate 1 step (you can add more)
    action = 1
    reward = 1.0

    total_reward += reward
    steps += 1

    # STEP block
    print(f"[STEP] step={steps} reward={reward}", flush=True)

    # END block
    print(f"[END] task={task_name} score={total_reward} steps={steps}", flush=True)


if __name__ == "__main__":
    main()



