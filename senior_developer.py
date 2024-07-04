class SeniorDeveloper:
    def __init__(self):
        self.complex_tasks = []
        self.simple_tasks = []
        self.code_monkey = None

    def handle_complex_task(self, task):
        self.complex_tasks.append(task)
        self.interact_with_gpt4(task)

    def delegate_simple_task(self, task):
        if self.code_monkey:
            self.code_monkey.handle_simple_task(task)
        else:
            self.simple_tasks.append(task)

    def interact_with_gpt4(self, task):
        # Placeholder for interacting with GPT-4 for complex tasks
        print(f"Interacting with GPT-4 for task: {task}")

    def set_code_monkey(self, code_monkey):
        self.code_monkey = code_monkey
