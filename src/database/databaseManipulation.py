import sqlite3

conn = sqlite3.connect('oinpUpdatesDatabase.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS updates (update_id blob, update_date text, update_data text)""")

# c.execute("INSERT INTO updates VALUES (:id, :date, :dataInfo)",
#            {'id': update2.id, 'date': update2.date, 'dataInfo': update2.updatetext})
# c.execute("SELECT * FROM updates WHERE date=:date", {'date': 'March 5, 2020'})
# DELETE FROM table_name WHERE condition; c.execute("DELETE FROM udates WHERE update_date='March 19, 2020'")
# print(c.fetchall())


def updateDatabase(newupdates):
    conn = sqlite3.connect('oinpUpdatesDatabase.db')
    c = conn.cursor()
    for update in newupdates:
        c.execute("INSERT INTO updates VALUES (:id, :date, :dataInfo)",
                  {'id': update['id'], 'date': update['date'], 'dataInfo': update['data']})
    conn.commit()
    conn.close()


def getUpdatesFromDatabase():
    conn = sqlite3.connect('oinpUpdatesDatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates")
    tempList = c.fetchall()
    conn.close()
    return tempList


def findUpdate(dataupdates, database):
    templist = []
    # numberofupdates = len(dataupdates) - len(database)
    for j in range(0, len(dataupdates)):
        if j < len(database):
            if database[j][0] != dataupdates[j]['id']:
                print('Database Error!')
                return 0
    for j in range(len(database), len(dataupdates)):
        templist.append(dataupdates[j])

    return templist
