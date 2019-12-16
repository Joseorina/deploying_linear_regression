import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CategoricalImputer(BaseEstimator, TransformerMixin):
    """
    Replaces categorical missing data(na)
    
    Arguments:
        BaseEstimator {[type]} -- [description]
        TransformerMixin {[type]} -- [description]
    """
    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X: pd.DataFrame, y:pd.Series = None) -> 'CategoricalImputre':
        """
        Fit statement to accomodate sklearn pipeline
        """
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        """
        Apply transformations to the dataframe
        """
        X = X.copy()
        for feature in self.variables:
            X[feature] =X[feature].fillna('Missing')
        return X            
        
class NumericalImputer(BaseEstimator, TransformerMixin):
    """
    Numerical missing values imputer
    """
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
            
    def fit(self, X, y=None):
        # persist mode in dictionary
        self.imputer_dict_ = {}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inpace=True)
        return X
                            