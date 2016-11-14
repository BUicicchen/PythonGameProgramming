import stafflib as sl
employeeList = []
day = [1, 0, 5, 366, 10]
#get the basic information for a new employee
employee = sl.new_employee('John', 'Sena', '30', '1', '11-Nov-2016', 'driver', '1000')
employee = sl.new_employee('John', 'Smith', '35', '0', '12-Nov-2016', 'codriver', '900')
employee = sl.new_employee('Maddie', 'Ziegler', '32', '5', '07-Nov-2016', 'cook', '1200')
employee = sl.new_employee('Avery', 'Wood', '29', '366', '11-Nov-2015', 'clerk', '1200')
employee = sl.new_employee('Lily', 'Green', '37', '10', '01-Nov-2016', 'researcher', '1300')

#replace the new information displayed to after deleting staffs
employee = sl.deleteStaff(employee)

days = sl.addDays()
sl.displayListEmployees(employee, day)
