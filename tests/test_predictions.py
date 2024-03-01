"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from sklearn.metrics import accuracy_score,r2_score

from housing_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    X_Test, y_test = sample_input_data
    expected_no_predictions = len(y_test)

    # When
    result = make_prediction(input_data=X_Test)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)

    assert isinstance(predictions[0], np.float32)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    _predictions = list(predictions)
   # y_true = y_test
    accuracy = r2_score(_predictions, y_test)
    print(accuracy)
    assert accuracy > 0.8

"""pred = model.predict(X_train_tfr)
print('linear train mse: {}'.format(mean_squared_error(y_train, pred)))
print('linear train rmse: {}'.format(sqrt(mean_squared_error(y_train, pred))))
print()
pred = model.predict(X_test_tfr)
print('linear test mse: {}'.format(mean_squared_error(y_test, pred)))
print('linear test rmse: {}'.format(sqrt(mean_squared_error(y_test, pred))))"""