import sqlite3
import os
import time

script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0]
rel_path = """./../../oinpUpdatesDatabase.db"""
# ^-- absolute dir the script is in
abs_file_path = os.path.join(script_dir, rel_path)
conn = sqlite3.connect(abs_file_path)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS updates (update_id blob, update_date text, update_data text)""")


# c.execute("INSERT INTO updates VALUES (:id, :date, :dataInfo)",
#            {'id': update2.id, 'date': update2.date, 'dataInfo': update2.updatetext})
# c.execute("SELECT * FROM updates WHERE date=:date", {'date': 'March 5, 2020'})
# DELETE FROM table_name WHERE condition; c.execute("DELETE FROM udates WHERE update_date='March 19, 2020'")
# print(c.fetchall())


def updateDatabase(newupdates):
    conn = sqlite3.connect(abs_file_path)
    c = conn.cursor()
    for update in newupdates:
        c.execute("INSERT INTO updates VALUES (:id, :date, :dataInfo)",
                  {'id': update['id'], 'date': update['date'], 'dataInfo': update['data']})
    conn.commit()
    conn.close()


def getUpdatesFromDatabase():
    conn = sqlite3.connect(abs_file_path)
    c = conn.cursor()
    c.execute("SELECT * FROM updates")
    tempList = c.fetchall()
    conn.close()
    return tempList


def findUpdate(dataupdates, database):
    localtime = time.asctime(time.localtime(time.time()))
    templist = []
    # numberofupdates = len(dataupdates) - len(database)
    for j in range(0, len(dataupdates)):
        if j < len(database):
            if database[j][0] != dataupdates[j]['id']:
                print(localtime, ': Database Error!')
                return 0
    for j in range(len(database), len(dataupdates)):
        templist.append(dataupdates[j])

    return templist


def findUpdates(dataupdates, database):
    conn = sqlite3.connect(abs_file_path)
    c = conn.cursor()
    templist = []
    newupdates = []
    dataUpdatesIndex = 0

    for i in range(0, len(dataupdates)):
        print(dataupdates[i]['id'])

        c.execute("SELECT update_id FROM updates WHERE update_id=:id", {id: str(dataupdates[i]['id'])})
        temp = []
        temp = c.fetchall()
        if not temp:
            newupdates.append(dataupdates[i])
        # found something new


def lastUpdatesMatch(dataupdates, database):
    # print(dataupdates[len(dataupdates) - 1]['date'])
    # print(database[len(database) - 1][1])
    # print(dataupdates[len(dataupdates) - 1]['data'])
    # print(database[len(database) - 1][2])

    if dataupdates[len(dataupdates) - 1]['id'] == database[len(database) - 1][0]:
        return True
    else:
        return False
