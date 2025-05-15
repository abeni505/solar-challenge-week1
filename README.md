# solar-challenge-week1

## 📦 How to Reproduce the Environment (Setup Instructions)

To set up this project on your local machine, follow the steps below.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2.. Create and activate conda environment:

Option A: Using venv
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Option B: Using Conda:
```bash
conda create -n solar-challenge python=3.10
conda activate solar-challenge
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Project Structure

The project is organized as follows:

```bash
solar-challenge-week1/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

### 5. Run the Code

Start exploring or running notebooks inside the notebooks/ folder, or use scripts inside scripts/ depending on the task.

💡 Tip: Make sure your virtual environment is active whenever working on the project.