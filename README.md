# WQP\_AICTE

# 💧 Water Quality Prediction Using Machine Learning

This project uses machine learning models to analyze and predict water quality parameters using historical data collected in Punjab, India (2000–2021). The goal is to build a predictive pipeline that not only forecasts specific chemical concentrations like Chloride (CL) but also classifies overall water quality and identifies anomalies.

## 📁 Files

* `WaterQualityPred.ipynb`: Jupyter Notebook containing complete data analysis, visualization, feature engineering, classification and regression models, seasonal analysis, anomaly detection, and export functions.
* `PB_All_2000_2021.csv`: Dataset with water quality metrics over the years from various regions in Punjab.
* `cleaned_water_quality.csv`: Final cleaned and enriched dataset with model outputs, seasonal labels, and anomaly detection.

## 📊 Dataset Overview

The dataset includes:

* Parameters: NH4, NO3, NO2, SO4, CL, BSK5, O2, PO4, Suspended solids, etc.
* Time Range: 2000 to 2021
* Coverage: Multiple locations and samples across Punjab

## 🔍 Project Highlights

* **Correlation Analysis**: Identified strongest chemical relationships (e.g., CL vs SO4)
* **Data Cleaning**: Linear interpolation for missing values
* **Predictive Modeling**: Used Random Forest for Chloride (CL) prediction
* **Feature Importance**: Visualized chemical impact on CL levels
* **Classification**: Classified water quality as Good, Moderate, or Poor using Logistic Regression
* **Seasonal Trend Analysis**: Boxplots of CL by season (Winter, Summer, etc.)
* **Anomaly Detection**: Detected unusual CL levels using Isolation Forest
* **Time Series Prep**: Monthly CL trend for future forecasting
* **Data Export**: Final enriched CSV for reporting or dashboards

## ⚙️ How to Run

1. Clone this repository or download the files.
2. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Open `WaterQualityPred.ipynb` in Jupyter or VS Code and run all cells.

## 📈 Model Goals

* Predict chloride (CL) levels based on chemical indicators.
* Categorize water quality using CL thresholds.
* Highlight seasonal and pollution trends.
* Detect pollution anomalies using unsupervised models.
* Export clean data for reuse and further analysis.

## 🔬 Technologies Used

* Python (Jupyter Notebook)
* Pandas, NumPy
* Scikit-learn
* Seaborn, Matplotlib

## 📌 Future Work

* Add LSTM/ARIMA for CL time-series forecasting
* Streamlit or Dash app for public interaction
* Integrate sensor/API real-time data pipelines

## 🧠 Author

Bathala Anjith Kumar
