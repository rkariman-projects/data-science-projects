import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from datetime import datetime

# ================================================
# 💾 Plot Auto-Save Utility — outside /src/
# ================================================
try:
    current_file = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
except NameError:
    project_root = os.path.dirname(os.getcwd())

if os.path.basename(project_root) == "src":
    project_root = os.path.dirname(project_root)

result_dir = os.path.join(project_root, "result")
plots_dir = os.path.join(result_dir, "plots")
os.makedirs(plots_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def save_plot(filename):
    full_path = os.path.join(plots_dir, f"{filename}_{timestamp}.png")
    plt.savefig(full_path, bbox_inches="tight", dpi=300)
    plt.close()
    print(f"✅ Plot saved to: {full_path}")

# ================================================
# 🧭 Visualization Functions
# ================================================

def plot_wind_direction(df):
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    theta = np.deg2rad(df["Wind Bearing (degrees)"])
    ax.hist(theta, bins=36, color='teal', alpha=0.7)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    plt.title("🧭 Wind Direction Frequency")
    save_plot("wind_direction")

def plot_main_distributions(df):
    features = ["Temperature (C)", "Humidity", "Wind Speed (km/h)", "Pressure (millibars)"]
    df[features].hist(bins=40, figsize=(10, 6), color="skyblue", edgecolor="black")
    plt.suptitle("📊 Distribution of Main Weather Features", fontsize=14)
    save_plot("main_feature_distributions")

def plot_correlation_heatmap(df):
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, cmap="coolwarm", annot=True, fmt=".2f")
    plt.title("🔥 Correlation Heatmap")
    save_plot("correlation_heatmap")

def plot_temperature_trends(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df.sample(1000), x="Formatted Date", y="Temperature (C)", color="orange")
    plt.title("🌡️ Temperature Variation Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    save_plot("temperature_trend")

def plot_monthly_avg(df):
    monthly_avg = df.groupby("Month")["Temperature (C)"].mean()
    monthly_avg.plot(kind="bar", color="skyblue")
    plt.title("📆 Average Monthly Temperature")
    plt.xlabel("Month")
    plt.ylabel("Avg Temp (°C)")
    save_plot("monthly_avg_temp")

def plot_weather_conditions(df):
    plt.figure(figsize=(8, 5))
    df["Summary"].value_counts().head(10).plot(kind="barh", color="lightgreen")
    plt.title("☁️ Top 10 Weather Conditions")
    plt.xlabel("Count")
    plt.ylabel("Condition")
    save_plot("top_weather_conditions")
