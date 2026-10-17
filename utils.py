import csv
import json

def read_csv(file: str) -> tuple[list[float], list[float]]:
    x: list[float] = []
    y: list[float] = []
    with open(file, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if row:
                x.append(float(row[0]))
                y.append(float(row[1]))
    return x, y

def load_params(file: str) -> tuple[float, float]:
    try:
        with open(file, "r") as f:
            params = json.load(f)
            return float(params["theta0"]), float(params["theta1"])
    except FileNotFoundError:
        return 0.0, 0.0
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        raise ValueError(f"corrupted or invalid parameter file '{file}': {e}")

def predict(mileage: float, theta0: float, theta1: float) -> float:
    return (theta0 + theta1 * mileage)
