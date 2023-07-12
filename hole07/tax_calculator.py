class TaxCalculator:
    def tax_for(self, gross_salary: float) -> float:
        class TaxBand:
            minimum_gross: float
            tax_rate: float

            def __init__(self, minium_gross, tax_rate):
                self.minimum_gross = minium_gross
                self.tax_rate = tax_rate

            def gross_to_tax_in_band(self, gross_salary_excluding_part_already_taxed_at_a_higher_rate: float) -> float:
                return max(0.0, gross_salary_excluding_part_already_taxed_at_a_higher_rate - self.minimum_gross)

            def gross_to_tax_in_bands_below_current(self, gross_salary: float) -> float:
                return min(gross_salary, self.minimum_gross)

            def tax_in_band(self, gross_salary_excluding_part_already_taxed_at_higher_rate: float) -> float:
                return round(
                    self.gross_to_tax_in_band(gross_salary_excluding_part_already_taxed_at_higher_rate) * self.tax_rate)

        upper_tax_band: TaxBand = TaxBand(40000, 0.4)
        upper_tax_bracket_tax: float = upper_tax_band.tax_in_band(gross_salary)
        remaining_gross_for_middle_and_lower_brackets: float = upper_tax_band.gross_to_tax_in_bands_below_current(gross_salary)

        middle_tax_band: TaxBand = TaxBand(20000, 0.2)
        middle_tax_bracket_tax: float = middle_tax_band.tax_in_band(remaining_gross_for_middle_and_lower_brackets)
        remaining_gross_for_lower_bracket: float = middle_tax_band.gross_to_tax_in_bands_below_current(remaining_gross_for_middle_and_lower_brackets)

        lower_tax_band: TaxBand = TaxBand(5000, 0.1)
        lower_tax_bracket_tax: float = lower_tax_band.tax_in_band(remaining_gross_for_lower_bracket)

        return lower_tax_bracket_tax + middle_tax_bracket_tax + upper_tax_bracket_tax


