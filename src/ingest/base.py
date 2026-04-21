#!/usr/bin/env python3

import pandas as pd
from typing import Optional
from abc import ABC, abstractmethod


class BaseDataLoader(ABC):
    """
    Implements the base class for all data loader interfaces.
    """
    def __init__(self) -> None:
        self.data = pd.DataFrame()
    

    @abstractmethod
    def load(self, path: Optional[str], db_conn_str: Optional[str]) -> pd.DataFrame:
        """
        Loads data from a database connection or from a CSV format file.

        Args:
            path (str | None) - the path to file to load data from.
            db_conn_str (str | None) - db connection string.
        
        Returns:
            Pandas DataFrame
        """
        raise NotImplementedError("Loader method not implemented.")

