class Car:
    fuel_type="petrol"
    def __init__ (self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def display(self):
        print("model:",self.model,"year:",self.year,"price:",self.price)
c1=Car("Thar",2024,2500000)
c2=Car("Honda",2023,2000000)
c1.display()
c2.display()

class Employee:
    employee_count=0
    def __init__(self):
        Employee.employee_count+=1
e1=Employee()
e2=Employee()
print(Employee.employee_count)


