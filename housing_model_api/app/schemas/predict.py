from typing import Any, List, Optional

from pydantic import BaseModel
from housing_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {'Id': [62],
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
    'FirstFlrSF': [581],
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
    'SaleCondition': ['Normal']

                    }
                ]
            }
        }
