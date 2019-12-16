from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler

import  prepocessors as pp

CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']

PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables = CATEGORICAL_VARS)),
    ]
)