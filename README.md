# Python Assignment Week 1: Employee Data Analysis

## Project overview
This project practises terminal commands, VS Code debugging, Jupyter timing, and a first exploratory analysis of the trainer-provided employee dataset.

## Dataset
The Day 3 employees.csv sample has 8 rows and 5 columns: id, name, department, salary, and city. The CSV is kept locally at project/data/employees.csv and is excluded from Git; add the trainer-provided file there before running the notebook.

## First data summary
- Shape: 8 rows by 5 columns.
- Numeric fields: id and salary; text fields: name, department, and city.
- The sample has no missing values and no duplicate rows.
- The notebook runs shape, info(), describe(), isna().sum(), and duplicated().sum().

## Business questions
1. Which department has the highest average salary?
2. Which department has the most employees?
3. Which city has the most employees?
4. How do salary ranges compare across departments?
5. Are missing or duplicate employee records affecting the analysis?

## Project files
- project/data/: local trainer dataset (not tracked by Git).
- project/notebooks/terminal_jupyter_practice.ipynb: notebook timing exercise.
- project/notebooks/terminal_jupyter_practice.py: nbconvert export.
- project/notebooks/employee_data_analysis.ipynb: employee data summary and questions.
- project/reports/: report output folder.
