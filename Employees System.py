from random import choice

from DistUpgrade.DistUpgradeCache import estimate_kernel_initrd_size_in_boot


def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print("Invalid Input, try again")
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print("Invalid Input, try again")
            else:
                return int(inp)
        else:
            return int(inp)



class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary



class EmployeesManager:
    def __init__(self):
        self.employess = []


    def add_employee(self):
        print('\nEnter the employee data:')
        name = input('Enter the name employee: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')
        self.employess.append(Employee(name, age, salary))


    def list_employee(self):
        if len(self.employess) == 0:
            print('\n No employees at the moment!')
            return
        print('\n Employee List')
        for emp in self.employess:
            print(emp.name, emp.age, emp.salary)


    def delet_employee_with_age(self, age_from, age_to):
        original_count = len(self.employess)
        self.employess = [
            emp for emp in self.employess if not (int(age_from) <= int(emp.age) <= int(age_to))
        ]
        deleted_count = original_count - len(self.employess)
        print(f'\nDeleted {deleted_count} employee(s) with age between {age_from} and {age_to}.')


    def find_employee_by_name(self, name):
        for emp in self.employess:
            if emp.name == name:
                return emp
        return None


    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('No employee wiht such a name')
        else:
            emp.salary = salary




class FrontEndManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print('\nProgramm Opetions:')
        masseges = [

            '1) Add a new Employee',
            '2) List all Employee',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'

        ]
        print('\n'.join(masseges))
        msg = f'Enter your choice (from 1 to {len(masseges)}): '
        return input_valid_int(msg, 1, len(masseges))


    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.employees_manager.add_employee()
            elif choice == 2:
                self.employees_manager.list_employee()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input('Enter age to: ')
                self.employees_manager.delet_employee_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')

                emp = self.employees_manager.find_employee_by_name(name)
                if emp is None:
                    print('No employee wiht such a name')
                    return

                salary = input_valid_int('Enter the salary: ')
                self.employees_manager.update_salary_by_name(name, salary)
            else:
                break







if __name__ == '__main__':
    app = FrontEndManager()
    app.run()