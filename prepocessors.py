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

class TemporalVariablesEstimator(self, X):
    """
    temporal variables calculator
    """
    def __init__(self, variables=None, reference_variable=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y= None):
        # we need this tep to fit to sklearn pipeline
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variables] - X[feature]
        return X

class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """
    rare label categorical encoder
    """
    def __init__(self, tol=0.05, variables=None):
        self.tol = tol
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        # persist frequent labels in dictionary
        self.encoder_dict_ = {}
        
        for var in self.variables:
            # the encoder will learn the most frequent categories
            t = pd.Series(X[var].value_counts() / np.float(len(X)))
            # frequent labels
            self.encoder_dict_[var] = list(t[t >= self.tol].index)
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(X[feature], X[feature], 'Rare')
            
        return X

class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """
    string to number categorical encoder
    """
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variable = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y):
        temp = pd.concat([X, y], axis=1)
        temp.columns = list(X.columns) + ['target']
        
        # persist tranforming dictionary(save to dictionary)
        self.encoder_dict_ = {}
        
        for var in self.variables:
            t = temp.groupby([var])['target'].mean().sort_values(
                ascending=True).index
            self.encoder_dict_[var] = {k: i for i, k in enumerate(t, 0)}
        
        return self
    
    def transform(self, X):
        # encode lables
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.encoder_dict_[feature])
        
        # check if the tranformer introducees NaN
        if X[self.variables].isnull().any().any():
            null_counts = X[self.variables].isnull().any()
            vars_ = {key: value for (key, value) in null_counts.items()
                     if value is True}
            raise ValueError(
                f'Categorical encoder has introduce Nan when '
                f'transforming categorical variables: {vars_.keys()}'    
            )
            
        return X
    
class LogTransformer(BaseEstimator, TransformerMixin):
    """
    logarithm transformer
    """
    
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
            
    def fit(self, X, y=None):
                    