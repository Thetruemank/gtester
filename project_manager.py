class ProjectManager:
    def __init__(self):
        self.project_idea = None
        self.clarifying_questions = []
        self.agents = {
            "senior_developer": None,
            "code_monkey": None,
            "qa_reviewer": None,
            "documentation": None
        }

    def take_project_idea(self, idea):
        self.project_idea = idea
        self.ask_clarifying_questions()

    def ask_clarifying_questions(self):
        # Placeholder for asking clarifying questions
        self.clarifying_questions = ["What is the main goal of the project?", "What are the key features?"]
        for question in self.clarifying_questions:
            print(question)

    def delegate_tasks(self):
        # Placeholder for delegating tasks to the appropriate agents
        if self.project_idea:
            print("Delegating tasks based on the project idea...")
            # Example delegation logic
            self.agents["senior_developer"] = "Handle complex tasks"
            self.agents["code_monkey"] = "Handle simpler tasks"
            self.agents["qa_reviewer"] = "Review code"
            self.agents["documentation"] = "Create documentation"
