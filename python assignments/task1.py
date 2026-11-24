import pandas as pd
import matplotlib.pyplot as plt

# Read employee information from the CSV file
employees = pd.read_csv("employees.csv")

# Remove extra spaces and make column names lowercase
employees.columns = employees.columns.str.strip().str.lower()

# Check that the columns needed for the charts exist
required_columns = {"id", "department", "salary"}
missing_columns = required_columns - set(employees.columns)

if missing_columns:
    raise ValueError(f"CSV is missing these columns: {missing_columns}")

# Convert ID and salary values to numbers
employees["id"] = pd.to_numeric(employees["id"], errors="coerce")
employees["salary"] = pd.to_numeric(employees["salary"], errors="coerce")

# Remove rows where ID, department, or salary is missing
employees = employees.dropna(subset=["id", "department", "salary"])


# 1. BAR CHART
average_salary = employees.groupby("department")["salary"].mean()

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(average_salary.index, average_salary.values, color="cornflowerblue")

# Add the required title and axis labels
ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")

ax.bar_label(bars, fmt="%.2f", padding=3)

fig.tight_layout()
fig.savefig("average_salary_by_department.png")
plt.close(fig)


# 2. HISTOGRAM
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(employees["salary"], bins=5, color="seagreen", edgecolor="black")
ax.set_title("Distribution of Salaries")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")

fig.tight_layout()
fig.savefig("salary_histogram.png")
plt.close(fig)


# 3. SCATTER PLOT
fig, ax = plt.subplots(figsize=(8, 5))

for department in employees["department"].unique():
    department_rows = employees[employees["department"] == department]

    ax.scatter(
        department_rows["id"],       # horizontal axis
        department_rows["salary"],   # vertical axis
        label=department,            # name shown in the legend
    )

ax.set_title("Employee ID vs Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department")

fig.tight_layout()
fig.savefig("id_vs_salary_by_department.png")
plt.close(fig)


# 4. LINE CHART
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o")

ax.set_title("Monthly Sales: January to June")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.grid(True)

fig.tight_layout()
fig.savefig("monthly_sales.png")
plt.close(fig)


print("Finished! Four PNG chart files have been saved.")