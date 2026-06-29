# 📊 Instagram Engagement Analytics for Alfido Tech

## Project Overview
This project is an end-to-end, production-ready Data Analytics solution designed to optimize the Instagram marketing strategy for **Alfido Tech**. Utilizing Python and advanced statistical analysis, the project transforms raw social media metrics into an actionable, data-driven content calendar and business strategy.

## Dataset
* **Source:** Kaggle (`bhanupratapbiswas/instgram` equivalent format)
* **Features:** Impressions, Likes, Comments, Shares, Saves, Profile Visits, Follows, Caption, Content Type, Date/Time (Derived).

## Objectives
* Identify the exact days and hours that yield peak engagement.
* Determine the highest-performing content formats and hashtag strategies.
* Deliver a professional Weekly Content Calendar.
* Formulate 5 actionable business strategies to accelerate growth.

## Business Problem
Despite regular posting, Alfido Tech faces stagnant audience growth and fluctuating engagement rates. They require empirical data analysis to stop "guessing" and start publishing strategically aligned with the Instagram algorithm's preferences.

## Tools Used
* **Language:** Python 3.9+
* **Data Manipulation:** Pandas, NumPy
* **Statistical Analysis:** SciPy
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Environment:** Jupyter Notebook

## Workflow
1. **Data Loading & Cleaning:** Handling nulls, duplicates, and standardizing schemas. (Dynamic timestamp generation implemented for incomplete time-series datasets).
2. **Feature Engineering:** Creating highly derived metrics (Engagement Rate, Weighted Engagement Score, Temporal categorizations).
3. **Exploratory Data Analysis:** Generation of 25+ professional plots (Heatmaps, Treemaps, KDEs, Regressions).
4. **Statistical Analysis:** Skewness, Kurtosis, and Covariance evaluations.
5. **Business Strategy Formulation:** Translating statistical insights into ROI-driven business rules.

## Key Insights
* Evening posts (17:00 - 19:30) statistically outperform morning posts by significant margins.
* 'Saves' have the highest correlation with overall algorithmic reach.
* High posting frequency negatively correlates with average engagement (Cannibalization effect).

## Recommendations
* Shift content mix to **40% Carousels, 40% Reels, 20% Images**.
* Post **4-5 times a week**, strictly during peak evening windows.
* Adopt a **"Golden Hour" response protocol** to boost algorithmic velocity.

## Project Structure
```text
├── dataset/
│   └── instagram.csv                     # Raw Kaggle Data
├── exports/
│   ├── Alfido_Tech_Instagram_Cleaned.csv # Engineered Data
│   └── Alfido_Tech_BI_Summary.csv        # Dashboard Aggregations
├── visualizations/                       # Generated Charts
├── Notebooks/
│   └── Instagram_Analytics_Alfido_Tech.ipynb # Main Python Pipeline
├── Documents/
│   └── Strategy_Document.md              # One-Page Business Report
├── README.md
└── requirements.txt
```

## Installation & How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your raw dataset named `instagram.csv` in the root directory.
4. Open the Jupyter Notebook:
   ```bash
   jupyter notebook Notebooks/Instagram_Analytics_Alfido_Tech.ipynb
   ```
5. Run all cells sequentially.

## Future Work
* Integrate the Instagram Graph API for real-time live data streaming.
* Apply VADER Sentiment Analysis to the comments section.
* Build a predictive Machine Learning model (XGBoost) to forecast post reach based on caption length, time, and format.
