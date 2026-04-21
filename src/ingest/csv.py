#!/usr/bin/env python3


import os
from typing import Optional
import pandas as pd

from .base import BaseDataLoader


class CSVLoader(BaseDataLoader):
    def load(self, path: Optional[str], db_conn_str: Optional[str]) -> pd.DataFrame:
        try:
            if not path:
                raise Exception(f"No Path provided for CSV source file.")

            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found on Path {path}")

            if not os.path.isfile(path) and not path.endswith(".csv"):
                raise Exception("Not a file.")

            self.data = pd.read_csv(path)

            return self.data
        except Exception as e:
            raise e
