from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Find this script's folder and the project folder
SCRIPT_FOLDER = Path(__file__).resolve().parent
PROJECT_FOLDER = SCRIPT_FOLDER.parent

# Look for employees.csv beside this script or in the project root
possible_csv_paths = [
    SCRIPT_FOLDER / "employees.csv",
    PROJECT_FOLDER / "employees.csv",
]
csv_path = next((path for path in possible_csv_paths if path.exists()), None)

if csv_path is None:
    raise FileNotFoundError(
        "Could not find employees.csv. Put it in the project folder "
        "or beside task1.py."
    )

# Read employee information from the CSV file
employees = pd.read_csv(csv_path)

# Clean column names: for example, " Department " becomes "department"
employees.columns = employees.columns.str.strip().str.lower()

# Check that the columns required for the charts exist
required_columns = {"id", "department", "salary"}
missing_columns = required_columns - set(employees.columns)

if missing_columns:
    raise ValueError(
        f"CSV is missing these columns: {', '.join(sorted(missing_columns))}"
    )

# Convert ID and salary values to numbers
employees["id"] = pd.to_numeric(employees["id"], errors="coerce")
employees["salary"] = pd.to_numeric(employees["salary"], errors="coerce")

# Remove rows with missing ID, department, or salary
employees = employees.dropna(subset=["id", "department", "salary"])

if employees.empty:
    raise ValueError("There are no valid employee rows to chart.")

# Make salary and ID numeric types suitable for plotting
employees["id"] = employees["id"].astype(int)
employees["salary"] = employees["salary"].astype(float)

# Calculate the average salary for each department
average_salary = employees.groupby("department")["salary"].mean()


# 1. BAR CHART: average salary per department
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(
    average_salary.index,
    average_salary.values,
    color="cornflowerblue",
)

ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.bar_label(bars, fmt="%.2f", padding=3)
ax.tick_params(axis="x", rotation=30)

fig.tight_layout()
fig.savefig(SCRIPT_FOLDER / "average_salary_by_department.png", dpi=300)
plt.close(fig)


# 2. HISTOGRAM: salaries grouped into exactly 5 bins
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(
    employees["salary"],
    bins=5,
    color="seagreen",
    edgecolor="black",
)

ax.set_title("Distribution of Salaries")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")

fig.tight_layout()
fig.savefig(SCRIPT_FOLDER / "salary_histogram.png", dpi=300)
plt.close(fig)


# 3. SCATTER PLOT: employee ID vs salary, coloured by department
fig, ax = plt.subplots(figsize=(8, 5))

for department in employees["department"].unique():
    department_rows = employees[employees["department"] == department]
    ax.scatter(
        department_rows["id"],
        department_rows["salary"],
        label=department,
    )

ax.set_title("Employee ID vs Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department")

fig.tight_layout()
fig.savefig(SCRIPT_FOLDER / "id_vs_salary_by_department.png", dpi=300)
plt.close(fig)


# 4. LINE CHART: monthly sales from January to June
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o", color="darkorange")

ax.set_title("Monthly Sales: January to June")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.grid(True, linestyle="--", alpha=0.5)

fig.tight_layout()
fig.savefig(SCRIPT_FOLDER / "monthly_sales.png", dpi=300)
plt.close(fig)


# BONUS: put all four charts together in one 2-by-2 figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Bar chart
dashboard_bars = axes[0, 0].bar(
    average_salary.index,
    average_salary.values,
    color="cornflowerblue",
)
axes[0, 0].set_title("Average Salary by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")
axes[0, 0].bar_label(dashboard_bars, fmt="%.2f", padding=3)
axes[0, 0].tick_params(axis="x", rotation=30)

# Histogram
axes[0, 1].hist(
    employees["salary"],
    bins=5,
    color="seagreen",
    edgecolor="black",
)
axes[0, 1].set_title("Salary Distribution")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Number of Employees")

# Scatter plot
for department in employees["department"].unique():
    department_rows = employees[employees["department"] == department]
    axes[1, 0].scatter(
        department_rows["id"],
        department_rows["salary"],
        label=department,
    )

axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend(title="Department")

# Line chart
axes[1, 1].plot(months, sales, marker="o", color="darkorange")
axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].grid(True, linestyle="--", alpha=0.5)

fig.tight_layout()
fig.savefig(SCRIPT_FOLDER / "four_charts_dashboard.png", dpi=300)
plt.close(fig)

print("Finished! Four charts and the combined dashboard were saved.")