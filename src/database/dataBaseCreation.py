import sqlite3
import json
from src.database.databaseManipulation import updateDatabase

conn = sqlite3.connect('oinpUpdatesDatabase.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS updates (update_id blob, update_date text, update_data text)""")
# cursor.execute("INSERT INTO updates VALUES ('test1_id1', 'test1_date1', 'test1_data1')")
# conn.commit()
# conn.close()

cursor.execute("SELECT * FROM updates")
print(cursor.fetchall())

# json_file = open('src\\data.json', 'r+')
# fileDataList = json.load(json_file)

# updateDatabase(fileDataList)

