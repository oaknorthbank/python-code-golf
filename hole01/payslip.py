class Payslip:
    sal: float

    def __init__(self, sal):
        self.sal = sal

    def get_net(self) -> int:
        ltbg: float = max(min(self.sal, 20000) - 5000, 0)
        mtbg: float = max(min(self.sal, 40000) - 20000, 0)
        utbg: float = max(self.sal - 40000, 0)
        return round(self.sal - (ltbg * 0.1 + mtbg * 0.2 + utbg * 0.4))
