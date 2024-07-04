class CodeMonkey:
    def __init__(self):
        self.simple_tasks = []

    def handle_simple_task(self, task):
        self.simple_tasks.append(task)
        self.interact_with_gpt35(task)

    def interact_with_gpt35(self, task):
        # Placeholder for interacting with GPT-3.5 for simpler tasks
        print(f"Interacting with GPT-3.5 for task: {task}")
