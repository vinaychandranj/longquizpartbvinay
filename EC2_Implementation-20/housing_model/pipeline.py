import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.pipeline import Pipeline
from feature_engine.imputation import ArbitraryNumberImputer, CategoricalImputer
from feature_engine.encoding import RareLabelEncoder,OrdinalEncoder
from feature_engine.selection import DropFeatures
from housing_model.config.core import config
from housing_model.processing.data_manager import TemporalVariableTransformer
from housing_model.processing.features import ElectricalNAHandler

import xgboost as xgb

#vars_dates = ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt']
#vars_cat = [var for var in X_train.columns if X_train[var].dtypes == 'O']
#vars_num = [var for var in X_train.columns if X_train[var].dtypes !='O' and var not in ['Id']]

housing_pipe = Pipeline([

  # ===== IMPUTATION =====
  # impute numerical variables with the ArbitraryNumberImputer
  ('ArbitraryNumber_imputation', ArbitraryNumberImputer( arbitrary_number=-1, variables='LotFrontage' )),
  ('handle_na', ElectricalNAHandler(variable='Electrical')),

  # impute numerical variables with the mostfrequent
  ('frequentNumber_imputation', CategoricalImputer(imputation_method='frequent', variables=config.model_config.vars_num, ignore_format=True)),

  # impute categorical variables with string missing
  ('missing_imputation', CategoricalImputer(imputation_method='missing', variables=config.model_config.vars_cat)),

  # == TEMPORAL VARIABLES ====
  ('elapsed_time', TemporalVariableTransformer(
      variables=['YearBuilt', 'YearRemodAdd', 'GarageYrBlt'], reference_variable='YrSold')),

  ('drop_features', DropFeatures(features_to_drop=['YearBuilt', 'YearRemodAdd', 'GarageYrBlt'])),

    # == CATEGORICAL ENCODING
  ('rare_label_encoder', RareLabelEncoder(tol=0.05, n_categories=5, variables=config.model_config.vars_cat)),
  # encode categorical and discrete variables using the target mean
  ('categorical_encoder', OrdinalEncoder(encoding_method='ordered', variables=config.model_config.vars_cat, unseen="encode")), #
  
  ('model_rf', xgb.XGBRegressor (n_estimators=config.model_config.n_estimators, max_depth=config.model_config.max_depth,objective='reg:squarederror',
                                    random_state=config.model_config.random_state))
])