import pandas as pd
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
    
    def fit(self, X:DataFrame, y:pd.Series = None) -> 'CategoricalImputre':
        """
        Fit statement to accomodate sklearn pipeline
        """
        return self
    
    def transform(self, X:pd.Dataframe) -> pd.DataFrame:
        """
        Apply transformations to the dataframe
        """
        X = X.copy()
        for feature in self.variables:
            X[feature] =X[feature].fillna('Missing')
        return X            
        
        