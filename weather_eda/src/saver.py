import os
from datetime import datetime

def save_results(df, temp_corr):
    """
    Save cleaned dataset and correlation matrix to /result/ (outside src).
    """
    try:
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    except NameError:
        project_root = os.getcwd()

    if os.path.basename(project_root) == "src":
        project_root = os.path.dirname(project_root)

    result_dir = os.path.join(project_root, "result")
    os.makedirs(result_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    clean_path = os.path.join(result_dir, f"cleaned_weather_{timestamp}.csv")
    corr_path = os.path.join(result_dir, f"correlation_{timestamp}.csv")

    df.to_csv(clean_path, index=False)
    temp_corr.to_csv(corr_path, header=True)

    print("✅ Files saved successfully at project root!")
    print(f"📁 Cleaned dataset: {clean_path}")
    print(f"📁 Correlation matrix: {corr_path}")
