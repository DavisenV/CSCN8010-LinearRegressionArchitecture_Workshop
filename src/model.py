import numpy as np
from sklearn.linear_model import LinearRegression

def train_regression_scratch(X_train, y_train, learning_rate=0.01, epochs=1000):
    """Trains a univariate linear regression model using gradient descent."""
    m = len(X_train)
    theta_0 = 0.0 # Intercept
    theta_1 = 0.0 # Slope

    for _ in range(epochs):
        predictions = theta_0 + theta_1 * X_train
        error = predictions - y_train
        
        grad_theta_0 = (1/m) * np.sum(error)
        grad_theta_1 = (1/m) * np.sum(error * X_train)
        
        theta_0 -= learning_rate * grad_theta_0
        theta_1 -= learning_rate * grad_theta_1

    return theta_0, theta_1

def predict_scratch(X_test, theta_0, theta_1):
    """Generates predictions using scratch weights."""
    return theta_0 + theta_1 * X_test

def train_regression_sklearn(X_train, y_train):
    """Trains a model using scikit-learn."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_sklearn(model, X_test):
    """Generates predictions using scikit-learn model."""
    return model.predict(X_test)

if __name__ == "__main__":
    print("Model module is import-safe and ready.")