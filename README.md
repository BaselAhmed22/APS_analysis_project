# APS Airline Passenger Satisfaction Analysis

## 1. Project Overview
It consists of traveler data divided into two types: train and test. This is usually the case when using machine learning, but here in our project, we limited ourselves to analysis and cleaning, so we merged the two types of data into one.

----------

## 2. Table of Contents
- [Project Overview](#1-project-overview)
- [Table of Contents](#2-table-of-contents)
- [Project Structure](#3-project-structure)
- [Dataset](#4-dataset)
- [Installation and Setup](#5-installation-and-setup)
- [How to Run](#6-how-to-run)
- [Key Findings](#7-key-findings)
- [Technologies Used](#8-technologies-used)

----------

## 3. Project Structure

```
APS_analysis/
│
├── .gitignore          # Specifies intentionally untracked files to ignore
├── data/               # Contains all data files for the project
│   ├── processed/      # Cleaned and preprocessed data
│   │   ├── cleaned_data.csv
│   │   ├── new_df.csv
│   │   └── outliers_summary.csv
│   │
│   └── raw/            # Original, immutable data
│       ├── test.csv
│       └── train.csv
│
├── notebooks/          # Jupyter notebooks for exploration and experimentation
│   ├── data_cleaning.ipynb
│   └── visualization.ipynb
│
├── scripts/            # Python scripts for automated tasks
│   ├── data_pipeline.py
│   └── run_analysis.py
│
├── src/                # Source code for the project
│   ├── __pycache__/
│   ├── data/           # Modules for data loading and cleaning
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── clean_data.py
│   │   └── load_data.py
│   │
│   └── eda/            # Modules for exploratory data analysis
│       ├── __pycache__/
│       ├── __init__.py
│       └── eda_utils.py
│
├── README.md           # Project overview and instructions
└── requirements.txt    # Project dependencies
```

----------

## 4. Dataset
- **Source:** [Kaggle Airline Passenger Satisfaction Dataset](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data)
- **Summary:** 2 files: train_data & test_data / 50 columns 
- **Features:** `Gender`, `Customer Type`, `Age`, `Type of Travel`, `Class`, `Flight Distance`, `Inflight wifi service`, `Departure/Arrival time convenient`, `Ease of Online booking`, `Seat comfort`, `Cleanliness`,`satisfaction`.

----------

## 5. Installation and Setup

To run this project locally, follow these steps:

**Step 1: Clone the repository**
```bash
git clone [Your GitHub Repository URL Here]
cd APS_analysis
```

**Step 2: Create and activate a virtual environment (recommended)**
```bash
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3: Install the required dependencies**
The project dependencies are listed in the `requirements.txt` file. Install them using pip:
```bash
pip install -r requirements.txt
```

----------

## 6. How to Run

There are two main ways to interact with this project:

### A. Run the Full Analysis Pipeline

To execute the entire data cleaning and analysis pipeline from start to finish, run the main script from the project's root directory:

```bash
python scripts/run_analysis.py
```
This script will:
1.  Load the raw data from `data/raw/`.
2.  Run the cleaning pipeline defined in `src/data/`.
3.  Generate and display all visualizations from `src/eda/`.

### B. Explore the Jupyter Notebooks

For a more interactive, step-by-step exploration of the data cleaning and visualization process, you can use the Jupyter Notebooks located in the `notebooks/` directory.

1.  Make sure your virtual environment is activated.
2.  Start Jupyter Lab or Jupyter Notebook:
    ```bash
    jupyter lab
    ```
3.  From the Jupyter interface, navigate to the `notebooks/` folder and open `data_cleaning.ipynb` or `visualization.ipynb`.

----------

## 8. Technologies Used

- **Python 3.x**
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical operations.
- **Matplotlib & Seaborn:** For data visualization.
- **Jupyter Notebook:** For interactive development and exploration.
