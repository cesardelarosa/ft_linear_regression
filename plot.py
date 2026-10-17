import matplotlib.pyplot as plt
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

def predict(mileage: float, theta0: float, theta1: float) -> float:
    return (theta0 + theta1 * mileage)

def plot(x: list[float], y: list[float], theta0: float, theta1: float):
    plt.scatter(x, y)
    plt.title("Car: Price vs. Mileage")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")

    x_min = min(x)
    x_max = max(x)
    y_min = predict(x_min, theta0, theta1)
    y_max = predict(x_max, theta0, theta1)
    plt.plot([x_min, x_max], [y_min, y_max], color="red", label="Regression line")

    plt.show()

def main():
    try:
        x, y = read_csv("data.csv")
        theta0, theta1 = load_params("params.json")
        plot(x, y, theta0, theta1)
    except ():
        pass

if __name__ == "__main__":
    main()
