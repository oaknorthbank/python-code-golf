from hole01.payslip import Payslip


def test_tax_is_zero_if_gross_is_below_tax_free_limit():
    payslip: Payslip = Payslip(5000)
    assert payslip.get_net() == 5000


def test_tax_on_amount_in_lower_tax_bracket_excludes_tax_free_limit():
    payslip: Payslip = Payslip(10000)
    assert payslip.get_net() == 9500
    payslip_2: Payslip = Payslip(20000)
    assert payslip_2.get_net() == 18500


def test_tax_on_amount_in_middle_tax_bracket_is_sum_of_lower_tax_bracket_amount_and_additional_middle_tax_bracket_amount():
    payslip: Payslip = Payslip(25000)
    assert payslip.get_net() == 22500
    payslip_2: Payslip = Payslip(40000)
    assert payslip_2.get_net() == 34500


def test_tax_on_amount_in_upper_tax_bracket_is_sum_of_lower_tax_bracket_amount_and_middle_tax_bracket_amount_and_additional_upper_tax_bracket_amount():
    payslip: Payslip = Payslip(50000)
    assert payslip.get_net() == 40500
    payslip_2: Payslip = Payslip(60000)
    assert payslip_2.get_net() == 46500
