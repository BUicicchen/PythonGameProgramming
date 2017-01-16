import csv

powerschoolDic = {'Teacher Name:':'', 'Section:':'Python', 'Assignment Name':'', 'Due Date:':'', 'Points Possible':'10', 'Extra Points:':'0', 'Score Type:':'Points', 'Student ID':'', 'Student Name:':'', 'Points':''}

'''GOOGLE CLASSROOM''' #---------------------------------------------------------

#open the file
gcFile = open('GoogleActivities.csv')
gcData = csv.reader(gcFile)
#show all the rows in the file
gcdata = []
for i, row in enumerate(gcData):
    gcdata.append(row)
    print('{}- '.format(i+1), end='')
    print(row)

# number of activities, assignments
gcassignmentList = []
gcNumberOfAssignments = len(gcdata[0]) - 3 # row 1, minus first 3 columes
for i, assignment in enumerate(gcdata[0]):
    if i >= 3:
        powerschoolDic['Assignment Name'] = gcassignmentList.append(assignment)


# due date ??????????????????
gcdateList = []
for colume, date in enumerate(gcdata[1]):
    if colume >= 3:
        from datetime import datetime
        date.strptime(date, '%d-%b-%y')
        gcdateList.append(date)
powerschoolDic['Due Date:'] = gcdateList



psFormat = "EEE MMM dd HH:mm:ss z yyyy"
gcFormat = "dd-mm-yy"
#24-Aug-16
#Thu Dec 01 00:00:00 CST 2016


# student names
gcnameList = []
for i, name in enumerate(gcdata):
    if i >= 3:
        powerschoolDic['Student Name'] = gcnameList.append(name[1] + ', ' + row[0])


# points
gcscoreList = []
for assignment in range(len(gcscoreList)):
    for i, points in enumerate(gcdata[2,8])-3:
        if i >= 3:
            powerschoolDic['Points'] = gcscoreList.append(float(points*0.1))

#close file
gcFile.close()








'''POWERSCHOOL''' #---------------------------------------------------------

# open the file
psFile = open('PowerSchool Template.csv')
psData = csv.reader(psFile)
#show all the rows in the file
psdata = []
for i, row in enumerate(psData):
    psdata.append(row)
    print('{}- '.format(i+1), end='')
    print(row)


# student ID
psstudentIDList = []
for i, studentID in enumerate(psdata):
    if i >= 9:
        for colume, id in enumerate(psdata[i]):
            powerschoolDic['Student ID'] = psstudentIDList.append(id)

#close file
psFile.close()


def converter(gcNumberOfAssignments):
    for assignment in range(gcNumberOfAssignments):

        # writer object responsible for converting the user’s data into delimited strings on the given file-like object
        with open('Assignment', str(gcNumberOfAssignments),'.csv', 'w+') as psFiles:

            pswriter = csv.writer(psFiles, delimiter=',')

            pswriter.writerow(['Teacher Name:'] + psdata[0][1])
            pswriter.writerow(['Section:'] + psdata[1][1])

            # PUT DIFFERENT ASSIGNMENTS????????????
            pswriter.writerow(['Assignment Name:'] + gcassignmentList[0,3])

            # DUE DATE ???????????????????????????
            pswriter.writerow(['Due Date:'] + ___________)

            pswriter.writerow(['Points Possible:'] + psdata[1][4])
            pswriter.writerow(['Extra Points:'] + psdata[1][5])
            pswriter.writerow(['Score Type:'] + psdata[1][6])
            pswriter.writerow('')
            pswriter.writerow(['Student ID'] + psdata[1][8] + psdata[2][8])

            for students in range(len(powerschoolDic['Student ID'])):
                pswriter.writerow([powerschoolDic['Student ID'][students]] + [powerschoolDic['Student Name:'][students]] + [powerschoolDic['Points'][students * gcNumberOfAssignments + i]])

        # psFiles.close()

converter(gcNumberOfAssignments)
