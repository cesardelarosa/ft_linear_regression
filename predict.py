from utils import load_params, predict

import sys

def get_mileage() -> float:
    raw = input("Enter mileage in km: ")
    mileage = float(raw)
    if mileage < 0:
        raise ValueError("mileage cannot be negative")
    return mileage

def main():
    try:
        mileage = get_mileage()
        theta0, theta1 = load_params("params.json")
        price = predict(mileage, theta0, theta1)
        print(f"The estimated car price is: {price:.2f}")
    except (ValueError, EOFError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        sys.exit("\nExecution interrupted by user.")

if __name__ == "__main__":
    main()
