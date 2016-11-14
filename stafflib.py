'''library for data representation, employee'''
employee = {'firstName':'', 'lastName':'', 'age':'', 'days':'', 'vinculatedSince':'', 'role':'', 'salary':''}
employeeList = []

def new_employee(first_name, last_name, age, days, vinculated_since, role, salary):
    #get the basic information for a new employee
    '''
    :param first_name:
    :param last_name:
    :param age:
    :param days:
    :param vinculated_since:
    :param role:
    :param salary:
    :return employee: the list of all employees
    '''
    employeeCopy = employee.copy()
    employeeCopy["firstName"] = first_name
    employeeCopy["lastName"] = last_name
    employeeCopy["age"] = age
    employeeCopy["days"] = days
    employeeCopy["vinculatedSince"] = vinculated_since
    employeeCopy["role"] = role
    employeeCopy["salary"] = salary
    employeeList.append(employeeCopy)
    return employeeList

def displayListEmployees(employeeList, day):
    '''
    :param employeeList: list that stores the basic information of each employee
    :param day: how many days had the employee worked
    :return: n/a
    '''
    print("Basic information of all employees: ")
    count = 0
    for i in employeeList:
        count += 1
        print("Staff #" + str(count))
        print(i["firstName"] + ' ' + i["lastName"] + ' age ' + i["age"] + ' has been working ' + str(day[count - 1]) + ' days since ' + i["vinculatedSince"] + ' as a ' + i['role'] + ' for USD' + i['salary'])
    print("Task Completed.")


def addDays():
    #This function adds one day to the employee's record of working days in this store when taking attendence
    '''
    :return: days in which each employee works at this store
    '''
    days = [1, 0, 5, 366, 10]
    addDay = raw_input("Are you taking attendence for today? (y/n) ")
    if(addDay == "y"):
        count = 0
        for i in days:
            i += 1
            days[count] = i
            count += 1
    return days

def deleteStaff(employeeList):
    #this function deletes the employee entered with number labeled
    '''
    :param employeeList: list that stores the basic information of each employee
    :return: list that stores the basic information of each employee who are left
    '''
    deleteEmployee = raw_input("Which employee will be deleted? (please enter with numbers or NO) ")
    if deleteEmployee == "NO":
        return employeeList
    else:
        employeeList.pop(int(deleteEmployee))
        return employeeList
