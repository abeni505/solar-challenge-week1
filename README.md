# solar-challenge-week1

## 📦 How to Reproduce the Environment (Setup Instructions)

To set up this project on your local machine, follow the steps below.

### 1. Clone the Repository

```bash
git clone https://github.com/abeni505/solar-challenge-week1.git
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
│   ├── __init__.py
│   ├── data_utils.py
│   └── eda_utils.py
├── notebooks/
│   ├── __init__.py
│   ├── togo_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── benin_eda.ipynb
│   └── compare_countries.ipynb
├── tests/
│   └── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
└── app/
    ├── __init__.py
    ├── main.py
    ├── utils.py
    └── dashboard_screenshots/

```

### Completed Tasks
## Task 1: Git & Environment Setup
Initialized GitHub repo with .gitignore, requirements.txt, and GitHub Actions CI.

Set up reproducible environment and folder structure.

## Task 2: EDA for Each Country
Performed profiling, cleaning, and visualization for Benin, Togo, and Sierra Leone.

Created detailed EDA notebooks with insights on GHI, DNI, DHI, ModA/B, wind, and temperature.

## Task 3: Cross-Country Comparison
Merged and compared cleaned datasets across all three countries.

Boxplots, summary statistics, and ANOVA tests included.

Insights highlight solar potential differences among countries.

## Bonus: Streamlit Dashboard
Built and deployed an interactive dashboard using Streamlit.

Features:

Country selector

Boxplots of GHI/DNI/DHI

Summary stats and top regions

Live Demo: https://solar-challenge-week1-abeni.streamlit.app/

### How to Use
Activate your virtual environment.

Open and run the EDA notebooks from the notebooks/ directory.

Launch the Streamlit dashboard locally with:

```bash
streamlit run app/main.py
```

📊 Dashboard Screenshot
Available in the repo under: app/dashboard_screenshots/