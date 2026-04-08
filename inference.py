from env import EmailEnv

env = EmailEnv()
tasks = [1, 2, 3]

print("[START] Running Evaluation")

for task_id in tasks:
    obs = env.reset(task_id)
    done = False
    total_reward = 0

    print(f"[STEP] Task {task_id} started")

    while not done:

        # Rule-based agent (no API needed)
        if task_id == 1:
            action = ["spam" if "free" in e.lower() or "offer" in e.lower() else "important" for e in obs]

        elif task_id == 2:
            action = []
            for e in obs:
                if "meeting" in e.lower():
                    action.append("work")
                elif "dinner" in e.lower():
                    action.append("personal")
                else:
                    action.append("promotions")

        elif task_id == 3:
            action = []
            for e in obs:
                if "urgent" in e.lower():
                    action.append({"priority": "high", "reply": "I will fix this issue"})
                else:
                    action.append({"priority": "low", "reply": "Sure, sounds good"})

        obs, reward, done, _ = env.step(action)
        total_reward += reward

    print(f"[STEP] Task {task_id} Score: {total_reward}")

print("[END] Evaluation Complete")