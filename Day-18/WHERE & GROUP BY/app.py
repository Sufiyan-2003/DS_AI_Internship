import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")

print("Filtered Interns:")
for row in cursor.fetchall():
    print(row)


cursor.execute("""
SELECT track, AVG(stipend) as avg_stipend
FROM interns
GROUP BY track
""")

print("\nAverage Stipend per Track:")
for row in cursor.fetchall():
    print(row)


cursor.execute("""
SELECT track, COUNT(*) as total_interns
FROM interns
GROUP BY track
""")

print("\nIntern Count per Track:")
for row in cursor.fetchall():
    print(row)

conn.close()
