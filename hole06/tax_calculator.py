class TaxCalculator:
    def tax_for(self, gross_salary: float) -> float:
        upper_tax_bracket_start: float = 40000
        upper_tax_bracket_rate: float = 0.4
        upper_tax_bracket_tax: float = self.tax_in_band(gross_salary, upper_tax_bracket_start, upper_tax_bracket_rate)
        remaining_gross_for_middle_and_lower_brackets: float = self.gross_to_tax_in_bands_below_current(gross_salary, upper_tax_bracket_start)

        middle_tax_bracket_start: float = 20000
        middle_tax_bracket_rate: float = 0.2
        middle_tax_bracket_tax: float = self.tax_in_band(remaining_gross_for_middle_and_lower_brackets, middle_tax_bracket_start, middle_tax_bracket_rate)
        remaining_gross_for_lower_bracket: float = self.gross_to_tax_in_bands_below_current(remaining_gross_for_middle_and_lower_brackets, middle_tax_bracket_start)

        lower_tax_bracket_start: float = 5000
        lower_tax_bracket_rate: float = 0.1
        lower_tax_bracket_tax: float = self.tax_in_band(remaining_gross_for_lower_bracket, lower_tax_bracket_start, lower_tax_bracket_rate)

        return lower_tax_bracket_tax + middle_tax_bracket_tax + upper_tax_bracket_tax

    def tax_in_band(self, gross_salary_excluding_part_already_taxed_at_higher_rate: float,
                    bracket_minimum_gross: float, tax_rate: float) -> float:
        return round(self.gross_to_tax_in_band(gross_salary_excluding_part_already_taxed_at_higher_rate, bracket_minimum_gross) * tax_rate)

    def gross_to_tax_in_bands_below_current(self, gross_salary: float, bracket_minimum_gross: float) -> float:
        return min(gross_salary, bracket_minimum_gross)

    def gross_to_tax_in_band(self, gross_salary_excluding_part_already_taxed_at_a_higher_rate: float, bracket_minimum_gross: float) -> float:
        return max(0.0, gross_salary_excluding_part_already_taxed_at_a_higher_rate - bracket_minimum_gross)


