class TaxCalculator:
    def tax_for(self, gross_salary: float) -> float:
        lower_tax_bracket_gross: float = max(min(gross_salary, 20000) - 5000, 0)
        middle_tax_bracket_gross: float = max(min(gross_salary, 40000) - 20000, 0)
        upper_tax_bracket_gross: float = max(gross_salary - 40000, 0)
        return round(lower_tax_bracket_gross * 0.1 + middle_tax_bracket_gross * 0.2 + upper_tax_bracket_gross * 0.4)