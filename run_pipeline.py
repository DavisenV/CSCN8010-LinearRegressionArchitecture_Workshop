# run_pipeline.py
import yaml
import sys
import pandas as pd
from src import preprocessing, model, evaluation

def main():
    # 1. Grab the config file name from the terminal command, default to ontario if none provided
    config_path = sys.argv[1] if len(sys.argv) > 1 else "configs/ontario_config.yaml"
    
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    print(f"Starting experiment: {config['experiment']['experiment_name']}")

    # 2. Load Processed Data
    df = pd.read_csv(config['data']['processed_csv_path'])

    # 3. Preprocess
    (X_train_scaled, X_test_scaled, 
     y_train_scaled, y_test_scaled, 
     scaler_y, X_test_unscaled, y_test_unscaled) = preprocessing.split_and_scale(
         df, 
         config['features']['predictor_col'], 
         config['features']['target_col'],
         test_size=config['preprocessing']['test_size']
     )

    # 4. Train Model (Using Scratch Implementation)
    theta_0, theta_1 = model.train_regression_scratch(
        X_train_scaled, 
        y_train_scaled, 
        learning_rate=config['model']['learning_rate'], 
        epochs=config['model']['epochs']
    )
    
    y_pred_scaled = model.predict_scratch(X_test_scaled, theta_0, theta_1)

    # 5. Evaluate
    y_pred_unscaled = scaler_y.inverse_transform(y_pred_scaled)
    rmse, mae, r2 = evaluation.calculate_metrics(y_test_unscaled, y_pred_unscaled)
    
    evaluation.print_metrics(rmse, mae, r2)

    # 6. Log Experiment
    evaluation.log_experiment(config, rmse, mae, r2)

if __name__ == "__main__":
    main()