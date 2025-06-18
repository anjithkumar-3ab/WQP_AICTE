# WQP_AICTE

# 💧 Water Quality Prediction Using Machine Learning

This project uses machine learning models to predict water quality parameters using historical water quality data from Punjab, India (2000–2021). The goal is to build predictive models that help monitor and manage water quality efficiently, especially in detecting harmful pollutants like TDS.

## 📁 Files

* `WaterQualityPred.ipynb`: Jupyter Notebook containing the complete data analysis, preprocessing, model training, and evaluation.
* `PB_All_2000_2021.csv`: Dataset containing water quality metrics collected over the years from multiple locations.

## 📊 Dataset Overview

The dataset includes:

* Water Quality Parameters: pH, TDS, EC, DO, BOD, and more.
* Temporal Coverage: 2000 to 2021.
* Spatial Coverage: Various districts and locations in Punjab.

## 🔍 Project Highlights

* **Data Cleaning**: Handling missing values and outliers.
* **Feature Engineering**: Selecting and scaling relevant features.
* **Visualization**: Trend analysis and correlation heatmaps.
* **Modeling**: Various regression models (e.g., Linear Regression, Random Forest, etc.).
* **Evaluation**: Metrics like MAE, MSE, R² for model comparison.

## ⚙️ How to Run

1. Clone this repository or download the files.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Open `WaterQualityPred.ipynb` in Jupyter Notebook or VS Code and run all cells.

## 📈 Model Goals

* Predict TDS (Total Dissolved Solids) based on other water quality indicators.
* Aid decision-makers in identifying areas with unsafe water.
* Provide early alerts through predictive modeling.

## 🔬 Technologies Used

* Python
* Jupyter Notebook
* Pandas, NumPy
* Scikit-learn
* Seaborn, Matplotlib

## 📌 Future Work

* Integrate deep learning models (LSTM for time-series).
* Add real-time data collection using APIs or sensors.
* Deploy the model via a web app for public use.

## 🧠 Author

Bathala Anjith Kumar
