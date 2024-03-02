from typing import List
import sys
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class ElectricalNAHandler(BaseEstimator, TransformerMixin):
    def __init__(self, variable):
        self.variable = variable
        
    def fit(self, X, y=None):
        # This method doesn't do anything in this case
        return self
    
    def transform(self, X):
        
        # Replace "NA" with a string representing missing values
        X[self.variable] = X[self.variable].replace('NA', 'MISSING')
        return X
