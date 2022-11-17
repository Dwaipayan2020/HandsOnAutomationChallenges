class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def explain(self):
        print(f'I am {self.f_name} {self.l_name} .\n')

    @property
    def email(self):
        email_id = f'{self.f_name}.{self.l_name}@codewidrony.com'
        print(f'email id : {self.f_name}.{self.l_name}@codewidrony.com\n')
        return email_id

    @email.setter
    def email(self, str_email):
        name = str_email.split('@')[0]
        self.f_name, self.l_name = name.split('.')[0], name.split('.')[1]
        email_id = f'{self.f_name}.{self.l_name}@codewidrony.com'
        # print(f' email id : {self.f_name}.{self.l_name}@codewidrony.com\n')
        return email_id

    @email.deleter
    def email(self):
        self.f_name, self.l_name = None, None





bengal_reporter = Employee('Dwaipayan', 'Das')
bengal_reporter.explain()
print(bengal_reporter.email)
bengal_reporter.f_name = 'Ronit'
bengal_reporter.explain()
print(bengal_reporter.f_name, bengal_reporter.l_name, end='\n')
print(bengal_reporter.email)
bengal_reporter.email = 'this.that@codewithrony.com'
print(bengal_reporter.email)
print(bengal_reporter.f_name, bengal_reporter.l_name, end='\n')
bengal_reporter.explain()


