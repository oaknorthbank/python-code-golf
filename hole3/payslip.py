class Payslip:
    gross_salary: float

    def __init__(self, gross_salary):
        self.gross_salary = gross_salary

    def get_net(self):
        return self.gross_salary - self.calculated_tax()

    def calculated_tax(self) -> int:
        lower_tax_bracket_gross: float = max(min(self.gross_salary, 20000) - 5000, 0)
        middle_tax_bracket_gross: float = max(min(self.gross_salary, 40000) - 20000, 0)
        upper_tax_bracket_gross: float = max(self.gross_salary - 40000, 0)
        return round(lower_tax_bracket_gross * 0.1 + middle_tax_bracket_gross * 0.2 + upper_tax_bracket_gross * 0.4)