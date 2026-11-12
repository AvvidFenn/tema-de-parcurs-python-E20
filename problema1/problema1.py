class Employee:
    """Common base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary, tasks):
        self.name = name
        self.salary = salary
        self.tasks = tasks 
        Employee.emp_count += 1

    def display_employee(self):
        print("Name:", self.name, ",Salary:", self.salary, ",Tasks:", list(self.tasks.keys()), ",Status:",list(self.tasks.values()))

# X = 5
# Y = 6

class Manager(Employee):
    mgr_count = 0
    def __init__(self, name, salary, tasks, position, departament):
        super().__init__(name, salary, tasks)
        self.position = position
        self.departament = departament
        Manager.mgr_count += 1

    def display_employee(self): # X % 6 = 5, deci afiseasa doar valorile de task-uri
        print(f'\nTask values for Manager {self.mgr_count}: {list(self.tasks.values())}')

if __name__ == "__main__":
    
    # Creare obiecte Employee
    emp1 = Employee("Gigi Maiorescu",4500, {"Task 1":"In progress"})
    emp2 = Employee("Ioana Anghel", 4300, {"Task 2":"Completed"})

    # Y/5 = 1 obiecte Manager cu Y/6 = 1 task(-uri)
    mgr1 = Manager("Elena Barav", 7000, {"Task 3":"In progress"}, "Team Leader", "Marketing")

    # Afisare angajati
    print("\nEmployee information display:")
    emp1.display_employee()
    emp2.display_employee()

    # Afisare manager, dar doar task-urile pt X % 6 = 5
    mgr1.display_employee()

    # Afisare emp_count si mgr_count
    print(f"\nThe value of emp_count for Employee 1 is: {emp1.emp_count}")
    print(f"\nThe value of mgr_count for Manager 1 is: {mgr1.mgr_count}")

