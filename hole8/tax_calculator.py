from __future__ import annotations

from typing import Optional


class TaxCalculator:
    def tax_for(self, gross_salary: float) -> float:
        lower_tax_band: TaxBand = TaxBand(5000, 0.1, None)
        middle_tax_band: TaxBand = TaxBand(20000, 0.2, lower_tax_band)
        upper_tax_band: TaxBand = TaxBand(40000, 0.4, middle_tax_band)
        return upper_tax_band.tax_for(gross_salary)


class TaxBand:
    minimum_gross: float
    tax_rate: float
    lower_tax_band: Optional[TaxBand]

    def __init__(self, minium_gross, tax_rate, lower_tax_band):
        self.minimum_gross = minium_gross
        self.tax_rate = tax_rate
        self.lower_tax_band = lower_tax_band

    def gross_in_band(self, gross_salary: float) -> float:
        return max(0.0, gross_salary - self.minimum_gross)

    def gross_to_tax_at_lower_band(self, gross_salary: float) -> float:
        return min(gross_salary, self.minimum_gross)

    def tax_for_band(self, gross_salary: float) -> float:
        return round(self.gross_in_band(gross_salary) * self.tax_rate)

    def tax_for_lower_bands(self, gross_salary: float) -> float:
        return self.lower_tax_band.tax_for(self.gross_to_tax_at_lower_band(gross_salary)) if self.lower_tax_band else 0

    def tax_for(self, gross_salary: float) -> float:
        return self.tax_for_band(gross_salary) + self.tax_for_lower_bands(gross_salary)
