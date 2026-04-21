#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Optional
import pandas as pd

class BaseDataPreprocessor(ABC):
    def __init__(
        self
    ) -> None:
        pass

    @abstractmethod
    def process(self, df: pd.DataFrame, columns: Optional[List[str]]) -> pd.DataFrame:
        """
        Preprocess any dataframe passed to it.

        Args:
            df (pd.DataFrame) - the pandas dataframe to process.
            columns (List of str or none) - the columns to preprocess
        
        Return:
            Pandas dataframe of preprocessed data.
        """
        raise NotImplementedError(f"")
