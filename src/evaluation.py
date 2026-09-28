import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
from pathlib import Path
from datetime import datetime

def calculate_metrics(y_true, y_pred):
    """Calculates RMSE, MAE, and R2 scores."""
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mae, r2

def print_metrics(rmse, mae, r2):
    """Nicely formats and prints the evaluation metrics."""
    print("--- Model Evaluation ---")
    print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
    print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
    print(f"R-squared (R2): {r2:.4f}")

def plot_regression(X_test_unscaled, y_test_unscaled, y_pred_unscaled):
    """Plots the actual scatter data against the predicted regression line."""
    plt.figure(figsize=(10, 6))
    
    plt.scatter(X_test_unscaled, y_test_unscaled, color='blue', alpha=0.5, label='Actual Data')
    plt.plot(X_test_unscaled, y_pred_unscaled, color='red', linewidth=2, label='Regression Line')
    
    plt.title('Predictor vs. Target')
    plt.xlabel('Predictor Feature')
    plt.ylabel('Target Variable')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Evaluation module is import-safe and ready.")

def log_experiment(config, rmse, mae, r2):
    """Appends experiment hyperparameters and metrics to a tracking CSV."""
    results_path = Path(config['experiment']['results_csv_path'])
    
    # Ensure the experiments directory exists
    results_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Compile the run data
    run_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "experiment_name": config['experiment']['experiment_name'],
        "predictor": config['features']['predictor_col'],
        "test_size": config['preprocessing']['test_size'],
        "learning_rate": config['model']['learning_rate'],
        "epochs": config['model']['epochs'],
        "rmse": round(rmse, 2),
        "mae": round(mae, 2),
        "r2": round(r2, 4)
    }
    
    df = pd.DataFrame([run_data])
    
    # Create new file with headers if it doesn't exist, otherwise append
    if not results_path.exists():
        df.to_csv(results_path, index=False)
    else:
        df.to_csv(results_path, mode='a', header=False, index=False)
    
    print(f"Experiment logged to {results_path}")