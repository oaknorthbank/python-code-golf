from hole08.payslip import Payslip
from hole08.tax_calculator import TaxCalculator


def test_tax_is_zero_if_gross_is_below_tax_free_limit():
    assert_net_given_gross(5000, 5000)


def test_tax_on_amount_in_lower_tax_bracket_excludes_tax_free_limit():
    assert_net_given_gross(10000, 9500)
    assert_net_given_gross(20000, 18500)


def test_tax_on_amount_in_middle_tax_bracket_is_sum_of_lower_tax_bracket_amount_and_additional_middle_tax_bracket_amount():
    assert_net_given_gross(25000, 22500)
    assert_net_given_gross(40000, 34500)


def test_tax_on_amount_in_upper_tax_bracket_is_sum_of_lower_tax_bracket_amount_and_middle_tax_bracket_amount_and_additional_upper_tax_bracket_amount():
    assert_net_given_gross(50000, 40500)
    assert_net_given_gross(60000, 46500)


def assert_net_given_gross(gross: int, expected_net: int):
    payslip: Payslip = Payslip(gross, TaxCalculator())
    assert payslip.get_net() == expected_net
