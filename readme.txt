# Interview Task – Mariam Mamdouh

## Project Overview
This repository contains the complete submission for the interview task, including UiPath workflows, Python script, and sample input/output files.  
The task is divided into four main parts: Excel Data Cleansing, Mails Consolidation, Web Automation, and Python analysis.

---

## Project Parts

### Part 1 – Excel Data Cleansing & Manipulation (UiPath)
- **Input file:** `Employees_Raw.xlsx`  
- **Tasks performed:**  
  - Remove duplicate rows.  
  - Standardize dates to `YYYY-MM-DD` format.  
  - Format phone numbers to `+20XXXXXXXXXX`.  
  - Trim extra spaces in names.  
- **Output file:** `Employees_Cleaned.xlsx`

---

### Part 2 – Mails Consolidation (UiPath)
- **Input file:** `Employees_Cleaned.xlsx`  
- **Tasks performed:**  
  - Split employees into two groups:  
    - Internal employees (`@corp.com`)  
    - External clients (any other domain)  
  - Create a new Excel with two sheets:  
    - Sheet 1: Internal employees  
    - Sheet 2: External clients  
- **Output file:** `Employees_Splitted.xlsx`

---

### Part 3 – Web Automation (UiPath)
- **Website:** [Yahoo Finance – Most Active Stocks](https://finance.yahoo.com/most-active)  
- **Tasks performed:**  
  - Extract Stock Symbol, Name, Price, Change, % Change, and Volume from the table.  
- **Output file:** `MostActiveStocks.xlsx`

---

### Part 4 – Python Coding Challenge
- **Input file:** `Employees_Cleaned.xlsx`  
- **Tasks performed:**  
  - Count the number of unique companies.  
  - Find the top 5 most common email domains.  
  - Count the number of employees per company.  
- **Output file:** `Summary_Report.csv`

---

### Part 5 – Submission & Documentation
- This repository includes:  
  1. `UiPath_Project.zip` – Full UiPath automation project.  
  2. `script.py` – Python analysis script.  
  3. Input + Output Excel/CSV files.  
  4. `README.md` – This file.

---

## How to Run
1. **UiPath Workflows:**  
   - Extract `UiPath_Project.zip` and open in UiPath Studio.  
   - Run the workflows in order:  
     1. Data Cleansing  
     2. Mails Consolidation  
     3. Web Automation  

2. **Python Script:**  
   - Ensure `Python 3.x` is installed.  
   - Run `script.py` in the same folder as `Employees_Cleaned.xlsx`.  
   - The script generates `Summary_Report.csv`.

---

## Assumptions
- Input Excel files are properly formatted.  
- UiPath Studio and Python 3.x are installed.  
- No missing dependencies for UiPath or Python scripts.

---

## Time Taken
Approx. X hours to complete the full task.
