from hole10.tax_calculator import TaxCalculator


class NullTaxCalculator(TaxCalculator):
    def tax_for(self, gross_salary: float) -> float:
        return 0
