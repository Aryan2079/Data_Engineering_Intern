# Create a DataFrame from a dictionary.
# Load a CSV file and display the first 5 rows.
# Select specific columns from a DataFrame.
# Filter rows where a column value is greater than a given number.
# Add a new column based on an existing column.
# Drop rows with missing values.
# Group by one column and calculate the average of another column.
# Merge two DataFrames on a common column.
# Convert a column to datetime format.
# Create a pivot table showing the average of one column grouped by two other columns.

import pandas as pd

# question 1
data = {
    "Name": ["Aryan", "Kafle", "Bigyan"],
    "Age": [23, 24, 25],
    "Salary": [50000, 40000, 30000]
}
df = pd.DataFrame(data)
print(df)

# question 2
df_scv = df.read_csv('data.csv')
print(df_scv)

# question 3
df_selected = df[["Name", "Salary"]]
print(df_selected)

# question 4
df_filtered = df[df["Age"] > 23]
print(df_filtered)

# question 5
df["Bonus"] = df["Salary"] * 1.1
print(df)

# question 6
df_with_nan = pd.DataFrame({
    "Name": ["Ram", "Hari", None],
    "Age": [25, None, 35]
})
df_clean = df_with_nan.dropna()
print(df_clean)

# question 7
df_group = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "IT"],
    "Salary": [50000, 70000, 55000, 80000]
})

avg_salary = df_group.groupby("Department")["Salary"].mean()
print(avg_salary)

# question 8
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Score": [85, 90, 95]
})

merged_df = pd.merge(df1, df2, on="ID", how="inner")
print(merged_df)

# question 9
df_dates = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "JoiningDate": ["2026-01-01", "2026-02-15"]
})

df_dates["JoiningDate"] = pd.to_datetime(df_dates["JoiningDate"])
print(df_dates)


# question 10
df_pivot = pd.DataFrame({
    "Region": ["North", "North", "South", "South"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 150, 200, 250]
})

pivot = pd.pivot_table(df_pivot, values="Sales", index="Region", columns="Product", aggfunc="mean")
print(pivot)

