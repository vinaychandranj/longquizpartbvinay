import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from housing_model import __version__ as _version
from housing_model.config.core import config
from housing_model.pipeline import housing_pipe
from housing_model.processing.data_manager import load_pipeline
from housing_model.processing.data_manager import pre_pipeline_preparation
from housing_model.processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
housing_pipe= load_pipeline(file_name=pipeline_file_name)


def make_prediction(*,input_data:Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """

    validated_data, errors = validate_inputs(input_df=pd.DataFrame(input_data))
    
    #validated_data=validated_data.reindex(columns=['Pclass','Sex','Age','Fare', 'Embarked','FamilySize','Has_cabin','Title'])
    validated_data=validated_data.reindex(columns=config.model_config.features)
    #print(validated_data)
    results = {"predictions": None, "version": _version, "errors": errors}
    
    predictions = housing_pipe.predict(validated_data)

    results = {"predictions": predictions,"version": _version, "errors": errors}
    print(results)
    if not errors:

        predictions = housing_pipe.predict(validated_data)
        results = {"predictions": predictions,"version": _version, "errors": errors}
        #print(results)

    return results

if __name__ == "__main__":

    data_in = {
    'Id': [62],
    'MSSubClass': [75],
    'MSZoning': ['RM'],
    'LotFrontage': [60],
    'LotArea': [7200],
    'Street': ['Pave'],
    'Alley': ['NA'],
    'LotShape': ['Reg'],
    'LandContour': ['Lvl'],
    'Utilities': ['AllPub'],
    'LotConfig': ['Inside'],
    'LandSlope': ['Gtl'],
    'Neighborhood': ['IDOTRR'],
    'Condition1': ['Norm'],
    'Condition2': ['Norm'],
    'BldgType': ['1Fam'],
    'HouseStyle': ['2.5Unf'],
    'OverallQual': [5],
    'OverallCond': [7],
    'YearBuilt': [1920],
    'YearRemodAdd': [1996],
    'RoofStyle': ['Gable'],
    'RoofMatl': ['CompShg'],
    'Exterior1st': ['MetalSd'],
    'Exterior2nd': ['MetalSd'],
    'MasVnrType': ['None'],
    'MasVnrArea': [0],
    'ExterQual': ['TA'],
    'ExterCond': ['TA'],
    'Foundation': ['BrkTil'],
    'BsmtQual': ['TA'],
    'BsmtCond': ['Fa'],
    'BsmtExposure': ['No'],
    'BsmtFinType1': ['Unf'],
    'BsmtFinSF1': [0],
    'BsmtFinType2': ['Unf'],
    'BsmtFinSF2': [0],
    'BsmtUnfSF': [530],
    'TotalBsmtSF': [530],
    'Heating': ['GasA'],
    'HeatingQC': ['TA'],
    'CentralAir': ['N'],
    'Electrical': ['SBrkr'],
    'FirststFlrSF': [581],
    'SecondFlrSF': [530],
    'LowQualFinSF': [0],
    'GrLivArea': [1111],
    'BsmtFullBath': [0],
    'BsmtHalfBath': [1],
    'FullBath': [3],
    'HalfBath': [1],
    'BedroomAbvGr': [3],
    'KitchenAbvGr': [1],
    'KitchenQual': ['Fa'],
    'TotRmsAbvGrd': [6],
    'Functional': ['Typ'],
    'Fireplaces': [0],
    'FireplaceQu': ['NA'],
    'GarageType': ['Detchd'],
    'GarageYrBlt': [1935],
    'GarageFinish': ['Unf'],
    'GarageCars': [1],
    'GarageArea': [288],
    'GarageQual': ['TA'],
    'GarageCond': ['TA'],
    'PavedDrive': ['N'],
    'WoodDeckSF': [0],
    'OpenPorchSF': [0],
    'EnclosedPorch': [144],
    'ThirdSsnPorch': [0],
    'ScreenPorch': [0],
    'PoolArea': [0],
    'PoolQC': ['NA'],
    'Fence': ['NA'],
    'MiscFeature': ['NA'],
    'MiscVal': [0],
    'MoSold': [3],
    'YrSold': [2007],
    'SaleType': ['WD'],
    'SaleCondition': ['Normal'],
    'SalesPrice': [101000]
}

    
    make_prediction(input_data=data_in)
