import sys
import json

def get_mileage() -> float:
    raw = input("Enter mileage in km: ")
    mileage = float(raw)
    if mileage < 0:
        raise ValueError("mileage cannot be negative")
    return mileage

def load_params(file: str) -> tuple[float, float]:
    try:
        with open(file, "r") as f:
            params = json.load(f)
            return float(params["theta0"]), float(params["theta1"])
    except FileNotFoundError:
        return 0.0, 0.0


def predict(mileage: float, theta0: float, theta1: float) -> float:
    return (theta0 + theta1 * mileage)

def main():
    try:
        mileage = get_mileage()
        theta0, theta1 = load_params("params.json")
        price = predict(mileage, theta0, theta1)
        print(f"The estimated car price is: {price:.2f}")
    except (ValueError, EOFError, KeyError, json.JSONDecodeError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        sys.exit("\nExecution interrupted by user.")

if __name__ == "__main__":
    main()
