def compute_reward(action, task):

    reward = 0

    if task["type"] in ["spam_detection", "categorization"]:
        correct = sum([a == b for a, b in zip(action, task["ground_truth"])])
        reward = correct / len(task["ground_truth"])

    elif task["type"] == "priority_reply":
        reward = 0

        for act, gt in zip(action, task["ground_truth"]):
            if act["priority"] == gt["priority"]:
                reward += 0.5

            keyword_hits = sum([1 for kw in gt["reply_keywords"] if kw in act["reply"]])
            reward += 0.5 * (keyword_hits / len(gt["reply_keywords"]))

        reward /= len(task["ground_truth"])

    return reward


def check_done(action, task):
    return True