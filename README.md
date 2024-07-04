# gtester

## Autonomous Development Team

This repository contains an autonomous development team that can take a project idea, ask clarifying questions, and delegate tasks to the appropriate agents. The team consists of the following agents:

- **Project Manager**: Responsible for managing the project, asking clarifying questions using GPT-4, and querying if more questions are needed, and delegating tasks to the appropriate agents.
- **Senior Developer**: Handles complex tasks and delegates simpler tasks to the Code Monkey. Interacts with GPT-4 for complex tasks.
- **Code Monkey**: Handles simpler coding tasks and interacts with GPT-3.5 for these tasks.
- **QA Reviewer**: Reviews code and ensures quality. Interacts with GPT-4 for QA tasks.
- **Documentation**: Creates and maintains project documentation. Interacts with GPT-3.5 for documentation tasks.

## How to Use

1. **Project Manager**: Start by providing the project idea to the Project Manager. The Project Manager will ask clarifying questions using GPT-4, query if more questions are needed, and delegate tasks to the appropriate agents.
2. **Senior Developer**: The Senior Developer will handle complex tasks and delegate simpler tasks to the Code Monkey. The Senior Developer interacts with GPT-4 for complex tasks.
3. **Code Monkey**: The Code Monkey will handle simpler coding tasks and interact with GPT-3.5 for these tasks.
4. **QA Reviewer**: The QA Reviewer will review the code and ensure quality. The QA Reviewer interacts with GPT-4 for QA tasks.
5. **Documentation**: The Documentation agent will create and maintain project documentation. The Documentation agent interacts with GPT-3.5 for documentation tasks.

Each agent is implemented in a separate Python file and can be run independently or as part of the autonomous development team.
