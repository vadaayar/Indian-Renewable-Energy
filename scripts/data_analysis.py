import os
import pandas as pd

# paths to the data files
DATA_DIR = os.path.join(os.getcwd(), 'data')
OUTPUT_DIR = os.path.join(os.getcwd(), 'output')

# file paths
broad_overview_path = os.path.join(DATA_DIR, "Broad_Overview_of_RE_Generation_September_2024-1.pdf")
irena_stats_path = os.path.join(DATA_DIR, "IRENA_Renewable_Energy_Statistics_2024 (3).pdf")
monthly_report_path = os.path.join(DATA_DIR, "Monthly_RE_Generation_Report_September_2024-1.pdf")
worldbal_doc_path = os.path.join(DATA_DIR, "WORLDBAL_Documentation.pdf")

def analyze_data():
    
    print(f"Broad Overview File: {broad_overview_path}")
    print(f"IRENA Stats File: {irena_stats_path}")
    print(f"Monthly Report File: {monthly_report_path}")
    print(f"WORLDBAL Documentation File: {worldbal_doc_path}")

if __name__ == "__main__":
    analyze_data()

