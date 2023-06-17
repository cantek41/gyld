"""
Deneme
"""
from abc import ABCMeta, abstractmethod
import pandas as pd


class AbstractData(metaclass=ABCMeta):

    @abstractmethod
    def load(self, query, param=None) -> pd.DataFrame:
        pass

    @abstractmethod
    def save(self, query, param=None) -> pd.DataFrame:
        pass
