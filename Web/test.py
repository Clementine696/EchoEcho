import sqlite3

# เชื่อมต่อ database
db_local = "Audio_DB.db"
connect = sqlite3.connect(db_local)
cursor = connect.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Soundpad (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Audio_name TEXT,
#         Audio_file TEXT,
#         Duration FLOAT
#     )
# ''')

cursor.execute("INSERT INTO Soundpad (Audio_name, Audio_file, Duration) VALUES (?, ?, ?)", ('MRE', 'MRE.mp3', 0.10))
connect.commit()
connect.close()