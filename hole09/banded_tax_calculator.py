from typing import Optional

from hole09.tax_calculator import TaxCalculator


class BandedTaxCalculator(TaxCalculator):
    minimum_gross: float
    tax_rate: float
    lower_band_calculator: Optional[TaxCalculator]

    def __init__(self, minium_gross, tax_rate, lower_band_calculator):
        self.minimum_gross = minium_gross
        self.tax_rate = tax_rate
        self.lower_band_calculator = lower_band_calculator

    def tax_for(self, gross_salary: float) -> float:
        return self.tax_for_band(gross_salary) + self.tax_for_lower_bands(gross_salary)

    def tax_for_lower_bands(self, gross_salary: float) -> float:
        return self.lower_band_calculator.tax_for(self.gross_to_tax_at_lower_band(gross_salary)) if self.lower_band_calculator else 0

    def gross_to_tax_at_lower_band(self, gross_salary: float) -> float:
        return min(gross_salary, self.minimum_gross)

    def tax_for_band(self, gross_salary: float) -> float:
        return round(self.gross_in_band(gross_salary) * self.tax_rate)

    def gross_in_band(self, gross_salary: float) -> float:
        return max(0.0, gross_salary - self.minimum_gross)







