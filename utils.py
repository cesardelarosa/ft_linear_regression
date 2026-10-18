import csv
import json
import math

DATA_FILE = "data.csv"
PARAMS_FILE = "params.json"

def read_csv(file: str = DATA_FILE) -> tuple[list[float], list[float]]:
    x: list[float] = []
    y: list[float] = []

    try:
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or "km" not in reader.fieldnames or "price" not in reader.fieldnames:
                raise ValueError(f"file '{file}' must contain 'km' and 'price' columns")
            for row in reader:
                if not row or row["km"] is None or row["price"] is None:
                    continue
                xi, yi = float(row["km"]), float(row["price"])
                if not math.isfinite(xi) or not math.isfinite(yi):
                    raise ValueError(f"non-finite value found in file '{file}'")
                if xi < 0 or yi < 0:
                    raise ValueError(f"negative value found in file '{file}'")
                x.append(xi)
                y.append(yi)
                
    except (StopIteration, IndexError):
        raise ValueError(f"file '{file}' is empty or has an invalid structure")
    except OSError as e:
        raise OSError(f"cannot read file '{file}': {e.strerror}")
    if not x:
        raise ValueError(f"file '{file}' contains no valid data points")

    return x, y

def load_params(file: str = PARAMS_FILE) -> tuple[float, float]:
    try:
        with open(file, "r") as f:
            params = json.load(f)
            return float(params["theta0"]), float(params["theta1"])
    
    except (json.JSONDecodeError, KeyError, ValueError, TypeError) as e:
        raise ValueError(f"corrupted or invalid parameter file '{file}': {e}")

def save_params(theta0: float, theta1: float, file: str = PARAMS_FILE) -> None:
    with open(file, "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f, indent=4)

def predict_price(mileage: float, theta0: float, theta1: float) -> float:
    return theta0 + theta1 * mileage

