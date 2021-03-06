class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12

class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def get_selary(self):
        return f'Total: {self.salary.get_total() + self.bonus}'