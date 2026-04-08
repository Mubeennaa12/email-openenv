def load_task(task_id):

    if task_id == 1:
        return {
            "type": "spam_detection",
            "input": [
                "Win a free iPhone now!!!",
                "Meeting at 3 PM",
                "Limited time offer!!!",
                "Project deadline extended"
            ],
            "ground_truth": ["spam", "important", "spam", "important"]
        }

    elif task_id == 2:
        return {
            "type": "categorization",
            "input": [
                "Team meeting tomorrow",
                "Dinner plans tonight?",
                "50% OFF sale!!!"
            ],
            "ground_truth": ["work", "personal", "promotions"]
        }

    elif task_id == 3:
        return {
            "type": "priority_reply",
            "input": [
                "Urgent: client issue needs fixing",
                "Casual catch-up later?"
            ],
            "ground_truth": [
                {"priority": "high", "reply_keywords": ["fix", "issue"]},
                {"priority": "low", "reply_keywords": ["later", "sure"]}
            ]
        }