import pandas as pd 

grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Missing Values:")
print(grades.isnull())

filled_grades = grades.fillna(0)

passed_students = filled_grades[filled_grades > 60]

# Output
print("\nOriginal Series:")
print(grades)

print("\nFilled Series:")
print(filled_grades)

print("\nScores Greater Than 60:")
print(passed_students)
