from hole09.tax_calculator import TaxCalculator


class Payslip:
    gross_salary: float
    tax_calculator: TaxCalculator

    def __init__(self, gross_salary, tax_calculator):
        self.gross_salary = gross_salary
        self.tax_calculator = tax_calculator

    def get_net(self):
        return self.gross_salary - self.tax_calculator.tax_for(self.gross_salary)
