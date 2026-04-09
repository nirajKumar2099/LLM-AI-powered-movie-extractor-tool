Project Details
Python Version: 3.13.7
Package Manager: uv (fast alternative to pip)
Primary Libraries: LangChain, OpenAI / Mistral / HuggingFace
Environment: Virtual Environment (.venv)
Entry Point: main.py
📂 Project Structure
LLM AI POWEREDTOOL-project/
│
├── main.py              # Main application logic
├── pyproject.toml       # Project configuration & dependencies
├── uv.lock              # Locked dependency versions
├── .python-version      # Python version (3.13.7)
├── README.md            # Documentation
├── .gitignore           # Ignore files
└── .venv/               # Virtual environment (auto-created by uv)
📄 Project Files Explained
File/Folder	Purpose
pyproject.toml	Defines dependencies, Python version, and project metadata
uv.lock	Locks exact versions for reproducible builds
main.py	Your main Python application
.python-version	Forces Python version (used by uv/pyenv)
.venv/	Virtual environment managed by uv
README.md	Setup and usage guide
⚙️ Setup Instructions
1️⃣ Install uv (if not installed)
pip install uv

👉 or (recommended)

pip install --upgrade uv
2️⃣ Initialize Project
uv init
3️⃣ Set Python Version
uv python install 3.13.7

Create file:

.python-version

Add:

3.13.7
4️⃣ Create Virtual Environment
uv venv
5️⃣ Activate Environment
▶️ Windows:
.venv\Scripts\activate
▶️ Mac/Linux:
source .venv/bin/activate
6️⃣ Add Dependencies

Example:

uv add langchain openai python-dotenv
This automatically updates:

pyproject.toml
uv.lock

Install all the package mentioned in requirements.txt 
uv pip install -r requirements.txt

7️⃣ Run Application
python main.py