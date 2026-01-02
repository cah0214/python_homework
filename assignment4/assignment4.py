import pandas as pd

# ----------------------------
# Task 1: Create a DataFrame
# ----------------------------
task1_data_frame = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})
print(task1_data_frame)

# Task 1: Add Salary column (copy first)
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

# Task 1: Increment Age column (copy first)
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)

# Task 1: Save to CSV without index
task1_older.to_csv("employees.csv", index=False)

# ----------------------------
# Task 2: Load CSV
# ----------------------------
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# Task 2: Load JSON employees
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# Task 2: Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# ----------------------------
# Task 3: Inspection
# ----------------------------
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

# ----------------------------
# Task 4: Data Cleaning
# ----------------------------
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

clean_data = dirty_data.copy()

# Remove duplicates
clean_data = clean_data.drop_duplicates()
print(clean_data)

# Convert Age to numeric (bad values -> NaN)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# Convert Salary to numeric and replace placeholders with NaN
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# Fill missing numeric values: Age with mean, Salary with median
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)

# Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(clean_data["Hire Date"].mode()[0])
print(clean_data)

# Strip whitespace and uppercase Name and Department
clean_data["Name"] = clean_data["Name"].astype(str).str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].astype(str).str.strip().str.upper()
print(clean_data)
