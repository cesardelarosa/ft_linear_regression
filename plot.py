from utils import load_params, predict, read_csv

import matplotlib.pyplot as plt

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

    plt.legend()
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
