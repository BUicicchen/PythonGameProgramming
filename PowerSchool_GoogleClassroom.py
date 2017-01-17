'''This program converts Google Classroom information into format on PowerSchool
One file is created for each assignment'''

import datetime
import csv

powerschoolDic = {'Teacher Name:':'', 'Section:':'', 'Assignment Name':'', 'Due Date:':'', 'Points Possible:':'', 'Extra Points:':'', 'Score Type:':'', 'Student ID':'', 'Student Name':'', 'Points':''}

'''GOOGLE CLASSROOM''' #---------------------------------------------------------

#open the Google Classroom file
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
gcNumberOfStudents = len(gcdata[0]) - 3 # colume 1, minus first 3 rows
for n, assignment in enumerate(gcdata[0]):
    if n >= 3:
        gcassignmentList.append(assignment)
powerschoolDic['Assignment Name'] = gcassignmentList

# Google Classroom date
gcdateList = []
dateString = ''
week = ['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for n, date in enumerate(gcdata[1]):
    if n >= 3:
        for mon in range(len(month)):
            if date[3:6] == month[mon]: # if it is characters 4~6
                numberOfMonth = mon + 1
        day = week[datetime.datetime(int('20' + date[-2:]), numberOfMonth, int(date[:2])).weekday()]
        dateString += day + ' ' + date[3:6] + ' ' + date[:2] + ' ' + '00:00:00 CST ' + '20' + date[-2:] # ps format
        dateString = ''
        gcdateList.append(dateString)
powerschoolDic['Due Date:'] = gcdateList

#date.strptime(date, '%d-%b-%y')
#psFormat = "EEE MMM dd HH:mm:ss z yyyy"
#gcFormat = "dd-mm-yy"
#24-Aug-16
#Thu Dec 01 00:00:00 CST 2016

# Google classroom student names
gcnameList = []
for i, name in enumerate(gcdata):
    if i >= 3:
        gcnameList.append(name[1] + ', ' + name[0])
powerschoolDic['Student Name'] = gcnameList

# Google Classroom points
gcscoreList = []
for assignment in range(len(gcnameList)):
    for i, points in enumerate(gcdata[gcNumberOfStudents+3]):
        if i >= 3:
            gcscoreList.append(int(points)/10)
powerschoolDic['Points'] = gcscoreList
#close the Google Classroom file
gcFile.close()



'''POWERSCHOOL''' #---------------------------------------------------------

# open the PowerSchool file
psFile = open('PowerSchool Template.csv')
psData = csv.reader(psFile)
#show all the rows in the file
psdata = []

for i, row in enumerate(psData):
    psdata.append(row)
    print('{}- '.format(i+1), end='')
    print(row)


# PowerSchool student ID
psstudentIDList = []
for i, studentID in enumerate(psdata):
    if i >= 9:
        for n, id in enumerate(psdata[i]):
            if n == 0:
                psstudentIDList.append(id)
powerschoolDic['Student ID'] = psstudentIDList
#close the PowerSchool file
psFile.close()



def newFiles(n):
    # create new files according to how many assignments
    '''
    :param n: int, number of assignments
    :return: name of files
    '''
    psFileName = 'Assignment '
    psFileName += str(n) + '.csv'
    return psFileName

def converter(n):
    # using information from Google Classroom to convert into PowerSchool format
    # write in the new .csv files created
    '''
    :param n: int, number of assignments
    :return: None
    '''

    for i in range(n):

        # writer object responsible for converting the user’s data into delimited strings on the given file-like object
        psFiles = open(newFiles(i+1), 'w')
        pswriter = csv.writer(psFiles, delimiter=',')


        # Teacher name
        powerschoolDic['Teacher Name:'] = list(psdata[0])
        pswriter.writerow(powerschoolDic['Teacher Name:'])

        # Section
        powerschoolDic['Section:'] = list(psdata[1])
        pswriter.writerow(powerschoolDic['Section:'])

        # Assignments
        for n, assignment in enumerate(powerschoolDic['Assignment Name']):
            if n == i:
                pswriter.writerow(['Assignment Name:'] + [assignment])

        # Due date
        for num, d in enumerate(powerschoolDic['Due Date:']):
            if num == i:
                pswriter.writerow(['Due Date:'] + [d])

        # Points possible
        powerschoolDic['Points Possible:'] = psdata[4][1]
        pswriter.writerow(['Points Possible:'] + [powerschoolDic['Points Possible:']])

        # Extra points
        powerschoolDic['Extra Points:'] = psdata[5][1]
        pswriter.writerow(['Extra Points:'] + [powerschoolDic['Extra Points:']])

        # Score type
        powerschoolDic['Score Type:'] = psdata[6][1]
        pswriter.writerow(['Score Type:'] + [powerschoolDic['Score Type:']])

        # Blank line
        pswriter.writerow([''])

        # Student ID
        pswriter.writerow(['Student ID'] + ['Student Name'] + ['Points'])

        # Student IDs
        for students in range(len(powerschoolDic['Student ID'])):
            pswriter.writerow([powerschoolDic['Student ID'][students]] + [powerschoolDic['Student Name'][students]] + [powerschoolDic['Points'][(students * gcNumberOfStudents) + i]])


converter(gcNumberOfStudents)
