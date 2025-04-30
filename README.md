# AutoDevMate - Hackathon Submission

## 📄 Written Problem and Solution Statement

### **Project Title:**  
**AutoDevMate – AI Assistant for Pull Request Reviews & Boilerplate Code Generation**

### **Problem & Opportunity**  
Software development teams often face two key productivity bottlenecks:  
1. Repetitive manual tasks like generating boilerplate code and project scaffolding  
2. The burden of reviewing pull requests (PRs) thoroughly and consistently  

Reviewing PRs is time-consuming, error-prone, and often suffers from human oversight or delay. Similarly, setting up project code from scratch is tedious and limits time for innovation. These issues collectively reduce developer velocity and satisfaction.

### **Solution Overview**  
**AutoDevMate** is an AI-powered assistant that streamlines software development by automatically reviewing PRs and generating clean, functional code scaffolds — using IBM Granite large language models at its core.

**Developers interact with AutoDevMate through:**  
- A **GitHub-integrated PR review bot**: Intelligently reviews code diffs, summarizes changes, and offers line-specific, human-like suggestions to improve clarity, correctness, and efficiency.  
- A **CLI or web assistant**: Instantly generates boilerplate code (e.g., REST APIs, React components, test suites) from natural language prompts.  
- An **interactive chat interface**, enabling developers to ask:
  - “What does this PR change?”
  - “Refactor this function to make it more readable.”
  - “Create a Dockerfile for this app.”

This reduces boring, repetitive tasks, improves code quality, and frees developers to focus on higher-level design and problem-solving.

### **Target Users**  
- Software engineers across all experience levels  
- Engineering managers aiming to improve code review workflows  
- DevOps and QA engineers automating validation tasks

### **Why It’s Unique & Creative**  
AutoDevMate is more than a code generator or linter — it mimics the critical thinking of experienced engineers. It provides contextual, nuanced feedback and builds entire project structures from vague ideas. Unlike rigid rule-based tools, it adapts to natural developer language and coding conventions.

By leveraging IBM Granite, AutoDevMate understands and generates enterprise-grade code, enabling a new level of AI assistance in the software lifecycle. It shortens review cycles, speeds up onboarding, and reduces burnout from menial dev work.

---

## 🧠 IBM Granite Usage Statement

**AutoDevMate** integrates IBM Granite large language models (LLMs) across three core components:

### 1. Pull Request Review Engine  
Granite is used to:  
- Summarize PR changes in plain language  
- Analyze diffs and provide optimization or security suggestions  
- Detect missing test cases and poor patterns by reasoning over logic and structure

Granite is prompted with full context (e.g., entire functions or classes) to provide actionable feedback, like a peer code reviewer.

### 2. Boilerplate Code Generator  
Granite LLMs generate complete code scaffolds from simple prompts such as:  
- “Create a Flask API with login and MongoDB integration”  
- “Generate a React login component with validation and styling”

It handles naming, folder structures, multi-file output, and stylistic consistency with minimal user input.

### 3. Developer Chat Assistant  
This chat interface enables real-time developer support using Granite:  
- Explain code, recommend refactors, or generate unit tests  
- Create Dockerfiles, CI/CD configs, or pipeline templates  
- Suggest alternate implementations or improve snippets

### **Why Granite?**  
IBM Granite models provide enterprise-grade reliability, contextual reasoning, and advanced natural language + code synthesis. Their robustness, accuracy, and performance across complex dev workflows make them ideal for real-world engineering use.

AutoDevMate demonstrates Granite’s potential to eliminate friction, save time, and transform mundane tasks into intelligent, automated workflows.

---

## Code setup:

1. Create python virtual environment.
2. Run pip install requirements.txt to install requirements.
3. on gitbash setup API keys as follows-
- export IBM_WATSONX_API_KEY=<Your_API_KEY>
- export IBM_WATSONX_PROJECT_ID=<Your_Project_key>
- export IBM_WATSONX_URL=https://us-south.ml.cloud.ibm.com
4. Run application using following command-
- streamlit run autodevmate.py

---

## Youtube Video-

- https://www.youtube.com/watch?v=Du1ZDCwVkK4



