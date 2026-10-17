from utils import load_params, predict, read_csv

import sys
import matplotlib.pyplot as plt

def plot(x: list[float], y: list[float], theta0: float | None, theta1: float | None):
    plt.scatter(x, y, color="blue", label="Data points")
    plt.title("Car: Price vs. Mileage")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")

    if theta0 is not None and theta1 is not None:
        x_min = min(x)
        x_max = max(x)
        y_min = predict(x_min, theta0, theta1)
        y_max = predict(x_max, theta0, theta1)
        plt.plot([x_min, x_max], [y_min, y_max], color="red", label="Regression line")

    plt.legend()
    plt.show()

def main():
    try:
        x, y = read_csv("data.csv")
        try:
            theta0, theta1 = load_params("params.json")
        except FileNotFoundError:
            print("Warning: 'params.json' not found. Showing data points only.", file=sys.stderr)
            theta0, theta1 = None, None
        plot(x, y, theta0, theta1)
    
    except (ValueError, OSError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
