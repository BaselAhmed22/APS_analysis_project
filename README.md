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
- [Key Findings and Insights](#7-Key-Findings-and-Insights)
- [Technologies Used](#8-technologies-used)
- [Run Notebooks in Google Colab](#9-run-notebooks-in-google-colab)

----------

## 3. Project Structure

```
APS_analysis/
│
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
│   ├── data/           # Modules for data loading and cleaning
│   │   ├── __init__.py
│   │   ├── clean_data.py
│   │   └── load_data.py
│   │
│   └── eda/            # Modules for exploratory data analysis
│       ├── __init__.py
│       └── eda_utils.py        
│
├── .gitignore          # Specifies intentionally untracked files to ignore
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

# Using VS Code Command Palette
1. Press Ctrl + Shift + P (or Cmd + Shift + P on macOS) to open the Command Palette.

2. Type "Python: Create Environment" and select it.

3. Choose Venv as the environment type.

4. Select the Python interpreter you want to use.

5. VS Code will automatically create and activate the virtual environment for you.
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

## 7. Key Findings and Insights
*(This is a section to summarize your results. Fill it with your notes.)*

* **Passengers are neutral or dissatisfied if the delay in arrival exceeds the departure time Conversely, they are satisfied when the delay is equal to the departure time.**

* **The level of satisfaction with the trip decreases as the trip category decreases. We find that:**
    1. **Business class:** 69.4% of customers are satisfied, while 30.6% are dissatisfied.  
    2. **Eco Plus class:** 24.6% of customers are satisfied, while 75.4% are dissatisfied.  
    3. **Eco class:** 18.8% of customers are satisfied, while 81.2% are dissatisfied.  

### Key Observations:
* **The percentage of female customers is higher than that of male customers.**
* **The percentage of loyal customers is higher than that of disloyal customers.**
* **The percentage of business trips is higher than that of personal trips.**
* **The percentage of neutral and dissatisfied customers is higher than that of satisfied customers.**



*(This is a section to summarize your results. Fill it with your insights.)*

Our analysis of passenger data reveals the customer experience. Satisfaction doesn't depend on a single factor, but on several, and most importantly, the quality of the experience during the journey.

### 1. The gap between travel classes
The results indicate a significant satisfaction gap between travel classes. This indicates that the airline is actually applying different service standards.

* **Business Class:** The vast majority of passengers (69.4%) are satisfied.
* **Economy Class and Eco Plus:** The situation is completely reversed for you, as the vast majority are neutral or dissatisfied (75.4% for Eco Plus and 81.2% for Eco).

**Vision:** The "economy class" experience fundamentally fails to meet passenger expectations. The extra amount paid for business class is not just for comfort, but for a satisfying journey, which is not the standard across the airline.

### 2. Primary Client:
The data clearly identifies the airline's core customer base.

* **Loyalty:** The majority of passengers are **loyal customers**, indicating a strong base of repeat business.
* **Purpose:** Most trips are for **business purposes**, not leisure.
* **Gender:** The passenger base leans slightly toward **females**.

**Vision:** The company's strategic efforts should focus heavily on retaining **loyal female travelers and business travelers**. Their needs must be the top priority.

### 3. The Paradox of Public Satisfaction
Despite having a loyal customer base who travel for work, the general feeling is negative.

* **Overall Judgment:** The majority of passengers across all classes combined are **neutral or dissatisfied**.

**Vision:** This is a serious warning sign. The airline is failing to meet the basic needs of its loyal customers. The dissatisfaction of a large number of economy class passengers reduces the overall perception of the brand, which could jeopardize long-term loyalty.

### 4. Punctuality:
The relationship between delay and satisfaction is more complex than expected.

* **Note:** Passengers tend to feel satisfied if the arrival delay is proportional to or less than the departure delay. Satisfaction decreases significantly when arrival delays exceed departure delays.

**Insight:** This suggests that passengers have a certain level of tolerance for delays, especially if they are "expected" (i.e., the arrival delay matches the initial departure delay). However, unexpected extensions of delays (such as long waits on the airport runway after landing) are a major source of frustration. Managing expectations and communication during the journey is essential.

----------

## 8. Technologies Used

- **Python 3.x**
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical operations.
- **Matplotlib & Seaborn:** For data visualization.
- **Jupyter Notebook:** For interactive development and exploration.

----------

## 9. Run Notebooks in Google Colab

### 1️⃣ Data Cleaning Notebook
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BaselAhmed22/APS_analysis_project/blob/main/notebooks/data_cleaning.ipynb)

### 2️⃣ Visualization Notebook
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BaselAhmed22/APS_analysis_project/blob/main/notebooks/visualization.ipynb)
