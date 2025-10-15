class Employee:
    total_employees = 0   

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1   

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")


class Math:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True



class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self._balance = amount



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e1.display_details()
e2.display_details()
Employee.show_total_employees()


print("Is 7 prime?", Math.is_prime(7))
print("Is 10 prime?", Math.is_prime(10))


acc = Account(1000)
print("Current Balance:", acc.balance)
acc.balance = 1500
print("Updated Balance:", acc.balance)
acc.balance = -200  


b1 = Book("Python Basics", "John Smith")
b2 = Book("AI Revolution", "Jane Doe")
b1.display()
b2.display()
