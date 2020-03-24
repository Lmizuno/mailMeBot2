from src.browser.browser import openBrowser, getRequest, parseJsonToString, getTextFromFindAll, fireIFTTT
from src.checksum.checksum import checksumList, checksumString
from src.database.databaseManipulation import getUpdatesFromDatabase, updateDatabase, findUpdate
from src.email.mail import emailUpdate, mailError
import time
import json

# browserInstance = openBrowser()

# time.sleep(4)
# body = browserInstance.find_element_by_css_selector('#pagebody')
# infoDates = browserInstance.find_elements_by_css_selector('#pagebody > h3')
# infoMonths = browserInstance.find_elements_by_css_selector('#pagebody > h2')

# bodyText = body.text

requestPage = getRequest()


bodyText = parseJsonToString(requestPage.text)
infoMonths = getTextFromFindAll(requestPage.text, 'h2')
infoDates = getTextFromFindAll(requestPage.text, 'h3')

dataList = bodyText.split('\n')

# clears the dataList
for i in range(0, len(dataList) - len(infoMonths)):
    for month in infoMonths:
        if dataList[i] == month:
            dataList.pop(i)
            break

for i in range(0, len(dataList)):
    for dates in infoDates:
        if dataList[i] == dates:
            dataList[i] = '\n'
            break

# joins the dataList into a string
tempStr = u''.join(dataList)
# split it again
updates = tempStr.split('\n')
# clears it from any empty string
for i in updates:
    if i == '':
        index = updates.index(i)
        updates.pop(index)


infoDates.reverse()
updates.reverse()

updatesList = []

for i in range(0, len(updates)):
    data = dict(id=checksumString(updates[i]), date=infoDates[i], data=updates[i])
    updatesList.append(data)

fileDataList = {}


# json_file = open('src\\data.json', 'r+')
# fileDataList = json.load(json_file)

# updateDatabase(fileDataList)

fileDataList = getUpdatesFromDatabase()
# copy data
# updatedList = fileDataList
isUpToDate = False
# get last update from both data sets and compare
lastUpdates = len(updatesList) - 1
lastDataInFile = len(fileDataList) - 1

newUpdatesList = findUpdate(updatesList, fileDataList)
if lastUpdates != lastDataInFile:
    if len(newUpdatesList) != 0:
        print('Update Found updating database and sending email')
        updateDatabase(newUpdatesList)
        emailUpdate(newUpdatesList)
        # IFTTT only the last one
        fireIFTTT(newUpdatesList[0]['date'], newUpdatesList[0]['data'])
    else:
        print('No new Update found')
else:
    print('same number of updates so far')

# browserInstance.close()
