# Renewable Energy Data Story

## Project Overview
This project analyzes India's renewable energy journey using interactive dashboards and Quarto for reproducibility. It highlights key trends in renewable energy, state-wise contributions, and global comparisons through engaging visualizations.

## Project Structure
This project includes the following components:
- **Quarto Report**: A detailed narrative, visualizations, and supporting data.
- **Slide Deck**: A presentation summarizing the key findings.
- **Reproducible Workflow**: Source code and data for transparency and scalability.

project-directory/ │ ├── dashboard/ # Interactive dashboard code │ ├── app.py # Main dashboard script │ ├── data/ # Raw data files │ ├── 20241029512325464.pdf │ ├── Broad_Overview_of_RE_Generation_September_2024-1.pdf │ ├── IRENA_Renewable_Energy_Statistics_2024.pdf │ ├── Monthly_RE_Generation_Report_September_2024-1.pdf │ ├── WORLDBAL_Documentation.pdf │ ├── output/ # Output folder for results (if needed) │ ├── quarto/ # Quarto report and presentation │ ├── index.qmd # Quarto report file │ ├── presentation.qmd # Quarto presentation file │ ├── references.bib # Bibliography file │ ├── scripts/ # Python scripts for analysis │ ├── data_analysis.py # Analysis script │ ├── data_preprocessing.py # Preprocessing script │ ├── venv/ # Python virtual environment │ ├── README.md # Project documentation ├── requirements.txt # Required Python packages


## Installation and Setup

### Clone the Repository:
```bash
git clone https://github.com/vadaayar/Indian-Renewable-Energy/upload/main
cd "PROJECT K"

Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate       # On Mac/Linux
.\venv\Scripts\activate        # On Windows

Install Required Packages:
pip install -r requirements.txt

Running the Dashboard
Navigate to the Dashboard Folder:
cd dashboard
Run the Application:
python app.py
Access the Dashboard:
Open your browser and go to: http://127.0.0.1:8050/
Rendering the Quarto Report
Install Quarto:
Download and install Quarto from quarto.org.

Render the Report:
Navigate to the quarto directory and run:
quarto render index.qmd
Additional Notes
Ensure you are using the correct Python version (>=3.7) for the virtual environment.
Data files in the data/ folder must match the structure expected in the Python scripts.
For troubleshooting, consult the documentation of Quarto and Dash.



Harish Kummara
Email: hkummara@constructor.university
