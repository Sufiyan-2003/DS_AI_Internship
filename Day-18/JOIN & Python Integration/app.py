import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

cursor.executemany("""
INSERT INTO mentors (mentor_name, track)
VALUES (?, ?)
""", [
    ("Dr. Sharma", "Data Science"),
    ("Mr. Khan", "Web Dev"),
    ("Ms. Iyer", "AI/ML"),
    ("Mr. Das", "Cyber Security")
])

conn.commit()

query = """
SELECT interns.name, interns.track, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

df = pd.read_sql_query(query, conn)

print("Joined Data:")
print(df)

conn.close()
