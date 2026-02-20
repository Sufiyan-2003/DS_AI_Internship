import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

cursor.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", [
    ("Sufiyan", "Data Science", 15000),
    ("Aisha", "Web Dev", 12000),
    ("Rahul", "AI/ML", 18000),
    ("Meera", "Cyber Security", 14000),
    ("Arjun", "Data Science", 16000)
])

conn.commit()

cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("Interns (Name & Track):")
for row in rows:
    print(row)

conn.close()
