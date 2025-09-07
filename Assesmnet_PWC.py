"""
employee_analysis.py

This script performs analysis on Employees_Cleaned.xlsx and generates a single summary report:
1. Counts the number of unique companies.
2. Finds the top 5 most common email domains.
3. Counts the number of employees per company.
4. Saves all results into one CSV file.

Author: Mariam Mamdouh
Date: 2025-09-06
"""

import os
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        raise

def main():

    base_path = os.path.dirname(os.path.abspath(__file__))

    # Input file
    file_path = os.path.join(base_path, 'Employees_Cleaned.xlsx')

    # Output file
    summary_file = os.path.join(base_path, 'Summary_Report.csv')

    # Load data
    df = load_data(file_path)

    # 1️⃣ Count unique companies
    unique_companies = df['Company'].nunique()

    # 2️⃣ Top 5 email domains
    df['Email_Domain'] = df['Email'].apply(lambda x: x.split('@')[-1])
    top_domains = df['Email_Domain'].value_counts().head(5)

    # 3️⃣ Employees per company
    employees_per_company = df['Company'].value_counts()

    # Prepare summary DataFrame
    summary_list = []

    # Add unique companies
    summary_list.append(['Number of Unique Companies', unique_companies])

    # Add top email domains
    for i, (domain, count) in enumerate(top_domains.items(), start=1):
        summary_list.append([f'Top Domain {i}: {domain}', count])

    # Add employees per company
    for company, count in employees_per_company.items():
        summary_list.append([f'Employees in {company}', count])

    summary_df = pd.DataFrame(summary_list, columns=['Metric', 'Value'])

    # Save single CSV
    summary_df.to_csv(summary_file, index=False)

    print(f"Summary report saved successfully: {summary_file}")

if __name__ == "__main__":
    main()
