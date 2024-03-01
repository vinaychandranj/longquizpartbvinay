
"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from housing_model.config.core import config
def test_age_variable_transformer(sample_input_data):
    print("Inside test features. No transformation is done here as everything done through pipeline")