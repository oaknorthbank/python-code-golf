from __future__ import annotations
from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def tax_for(self, gross_salary: float) -> float:
        pass
