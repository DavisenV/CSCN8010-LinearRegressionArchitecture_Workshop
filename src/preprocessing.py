import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_and_format(df, x_col, y_col):
    """Removes nulls, strips commas, and converts text to numbers."""
    df_clean = df[[x_col, y_col]].dropna().copy()
    df_clean[x_col] = pd.to_numeric(df_clean[x_col].astype(str).str.replace(',', '', regex=False), errors='coerce')
    df_clean[y_col] = pd.to_numeric(df_clean[y_col].astype(str).str.replace(',', '', regex=False), errors='coerce')
    return df_clean.dropna()

def split_and_scale(df, x_col, y_col, test_size=0.2):
    """Splits data into train/test sets and scales it to standard normally distributed data."""
    X = df[x_col].values.reshape(-1, 1)
    y = df[y_col].values.reshape(-1, 1)

    # 1. Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # 2. Scale
    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_train_scaled = scaler_X.fit_transform(X_train)
    X_test_scaled = scaler_X.transform(X_test)
    
    y_train_scaled = scaler_y.fit_transform(y_train)
    y_test_scaled = scaler_y.transform(y_test)

    # We return the original X_test and y_test for plotting later, plus scaler_y to un-scale predictions
    return X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled, scaler_y, X_test, y_test

if __name__ == "__main__":
    print("Preprocessing module is import-safe and ready.")