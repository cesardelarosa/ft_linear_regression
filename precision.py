import math
import sys

from utils import load_params, predict, read_csv

def mean_squared_error(y: list[float], y_hat: list[float]) -> float:
    return sum((yi - y_pred) ** 2 for yi, y_pred in zip(y, y_hat)) / len(y)

def mean_absolute_error(y: list[float], y_hat: list[float]) -> float:
    return sum(abs(yi - y_pred) for yi, y_pred in zip(y, y_hat)) / len(y)

def root_mean_squared_error(y: list[float], y_hat: list[float]) -> float:
    return math.sqrt(mean_squared_error(y, y_hat))

def variance(y: list[float]) -> float:
    y_mean = sum(y) / len(y)
    return sum((yi - y_mean) ** 2 for yi in y) / len(y)

def r2_score(y: list[float], y_hat: list[float]) -> float:
    var = variance(y)
    if var == 0:
        return 0.0
    return 1 - mean_squared_error(y, y_hat) / var

def main():
    try:
        x, y = read_csv("data.csv")
        theta0, theta1 = load_params("params.json")
        y_hat = [predict(xi, theta0, theta1) for xi in x]
        
        r2 = r2_score(y, y_hat)
        rmse = root_mean_squared_error(y, y_hat)
        mae = mean_absolute_error(y, y_hat)
        
        print(f"R^2 = {r2:.4f}")
        print(f"RMSE = {rmse:.2f}")
        print(f"MAE = {mae:.2f}")
    
    except (ValueError, OSError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
