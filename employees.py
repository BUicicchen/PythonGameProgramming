class Employee:
    numOfEmps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ',' + last + '@company.com'

        Employee.numOfEmps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # additional constructors
    @classmethod
    def fromtimestamp(cls,t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y,m,d)

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)
'''
    @classmethod
    def fromordinal(cls, n):
'''

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

class Engineer(Employee):
    raise_amt = 1.10
    numOfEngineers = 0
    def __init__(self, first, last, pay, department, certification):
        super().__init__(first,last,pay)
        self.department = department
        self.certificatoin = certification
        Engineer.numOfEngineers += 1

    @classmethod
    def how_many_engineers(cls):
        print('The number of engineers is:' , cls.numOfEngineers)



eng1 = Engineer('Testing', 'Name', 70000, 'Science','yes')
print(eng1.how_many_engineers())

'''
@implements_to_string
class HTTPException(Exception):
    code = None
    description = None
    def __init__(self, description=None, response=None):
        Exception.__init__(self)
        if description is not None:
            self.description = description
        self.response = response

    @classmethod
    def wrap(cls, exception, name=None):
        class newcls(cls, exception):
            def __init__(self, arg=None, *args, **kwargs):
                cls.__init__(self,*args,**kwargs)
                exception.__init__(self,arg)
        newcls.__module__ = sys._getframe(1).f_globals.get('__name__')
        newcls.__name__ = name or cls.__name__ + exception.__name__
        return  newcls
    @property
    def name(self):
        return HTTP_STATUS_CODES.get(self.code, 'Unknown Error')

    def get_description(self, environ=None):
        return u'<p>%s</p>' % escape(self.description)

    def get_body(self, eviron=None):
        return text_type((
            u''
        ))
'''
