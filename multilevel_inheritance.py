class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def person_info(self):
        return {"name" : self.name,
                "age" : self.age}


class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def employee_info(self):
        details = super().person_info()
        details["salary"] = self.salary
        return details
        

class Manager(Employee):
    def __init__(self,name,age,salary ,department):
        super().__init__(name,age,salary)
        self.department = department
    
    def manager_info(self):
        details = super().employee_info()
        details["department"] = self.department
        return details

m = Manager("varun",21,50000,"AI")
print(m.manager_info())
                
        
