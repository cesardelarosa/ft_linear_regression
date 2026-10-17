from utils import load_params, predict

import math
import sys

def get_mileage() -> float:
    raw = input("Enter mileage in km: ")
    mileage = float(raw)
    
    if not math.isfinite(mileage) or mileage < 0:
        raise ValueError("mileage must be a finite non-negative number")
    
    return mileage

def main():
    try:
        mileage = get_mileage()
        try:
            theta0, theta1 = load_params("params.json")
        except FileNotFoundError:
            theta0, theta1 = 0.0, 0.0
        price = predict(mileage, theta0, theta1)
        print(f"The estimated car price is: {price:.2f}")
    
    except (ValueError, OverflowError, OSError, EOFError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
