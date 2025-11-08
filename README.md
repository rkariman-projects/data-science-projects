# 🌦️ Weather EDA Project


  

🚀 Overview

1️⃣ Data Loading

Handled by src/data_loader.py:


Automatic project-root detection

Portable across machines & environments

Robust CSV loading with Pandas


2️⃣ Preprocessing

Logic inside src/preprocess.py:


Cleaning missing values

Datetime parsing

Feature engineering:

Temp_Diff

is_Rainy

Year, Month, Hour




Outlier detection using IQR

Temperature correlation extraction


3️⃣ Visualization

All plotting handled by src/visualizer.py:


🧭 Wind direction polar plot

🌡️ Temperature variation over time

📊 Distributions of key weather variables

🔥 Correlation heatmap

📆 Monthly average temperature

☁️ Top weather conditions


All plots are auto-saved in result/plots/ with timestamps.

4️⃣ Automated Saving


Cleaned dataset → cleaned_weather_<timestamp>.csv

Correlation matrix → correlation_<timestamp>.csv

Plots → saved via save_plot() utility



📦 Installation

        
        bash
        
    
  
      pip install -r requirements.txt
    
    
  
  

▶️ How to Use

Option A — Run the Jupyter Notebook (Recommended)


Open:


        
        awk
        
    
  
      weather_eda/notebooks/weather_analysis.ipynb
    
    
  
  

Run all cells.


The notebook will automatically:


✅ Load & preprocess data

✅ Generate all plots

✅ Save CSV outputs

✅ Store results in result/



🧩 Module Descriptions

data_loader.py


Detects correct project root

Loads weatherHistory.csv safely

Returns a Pandas DataFrame


preprocess.py


Handles missing values & datetime conversion

Performs feature engineering & outlier detection

Extracts temperature correlations


visualizer.py


Wind polar charts

Histograms & line charts

Heatmaps & bar plots

Auto-saves with timestamp



📊 Example Outputs

Plot Type	 | 	File Name Example
-------------------------------
Wind Direction Polar	 | 	wind_direction_2023-11-08_14-35-22.png
Correlation Heatmap	 | 	correlation_heatmap_2023-11-08_14-35-22.png
Monthly Temperature	 | 	ave_temperature_2023-11-08_14-35-22.png
Top Weather Conditions	 | 	top_weather_conditions_2023-11-08_14-35-22.png

✅ Requirements

See:

        
        mizar
        
    
  
      requirements.txt
    
    
  
  

⭐ Future Improvements


[ ] ML-based temperature prediction

[ ] Interactive plots with Plotly

[ ] Weather API via FastAPI

[ ] Unit tests for all modules in src/

[ ] Add Dockerfile for containerization



✨ Author

Kariman — Data Science Studentist & Python Developer


  
  

