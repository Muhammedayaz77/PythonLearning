import sqlite3

# Create or open the SQLite database.
connectionObj = sqlite3.connect("test_DataBase.db")
cursorObj = connectionObj.cursor()

# Create the table if it does not already exist.
cursorObj.execute("""
CREATE TABLE IF NOT EXISTS student (
    studentIdInt INTEGER PRIMARY KEY AUTOINCREMENT,
    studentNameStr TEXT NOT NULL,
    studentClassStr TEXT NOT NULL
)
""")
connectionObj.commit()

# Insert a student record.
cursorObj.execute(
    "INSERT INTO student (studentNameStr, studentClassStr) VALUES (?, ?)",
    ("Ayaz", "Python")
)
connectionObj.commit()

# Read records from the table.
cursorObj.execute("SELECT * FROM student")
studentList = cursorObj.fetchall()
for studentTuple in studentList:
    print("Student:", studentTuple)

# Update a student record.
cursorObj.execute(
    "UPDATE student SET studentClassStr = ? WHERE studentIdInt = ?",
    ("Python Beginner", 1)
)
connectionObj.commit()

# Delete a student record when needed.
# cursorObj.execute("DELETE FROM student WHERE studentIdInt = ?", (1,))
# connectionObj.commit()

# Close the database connection.
cursorObj.close()
connectionObj.close()
print("Database operation complete")
