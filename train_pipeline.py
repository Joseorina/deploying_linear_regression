import pathlib

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

import pipeline

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_model'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'SalePrice'

FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
            'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
            'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
            '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
            'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageCars', 'PavedDrive', 'LotFrontage',
            # this variable is only to calculate temporal variable:
            'YrSold']

def save_pipeline() -> None:
    """
    persist the pipeline
    """
    pass

def run_training() -> None:
    print('Training ... ')
    
if __name__ == "__main__":
    run_training()    