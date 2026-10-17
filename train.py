import math
import json

def normalize(values: list[float]) -> tuple[list[float], float, float]:
    return

def gradient_descent(x: list[float], y: list[float],
    alpha: float, epochs: int, eps: float) -> tuple[float, float]:
    return

def denormalize(theta0: float, theta1: float,
    x_min: float, x_max: float) -> tuple[float, float]:
    return

def save_params(file: str, theta0: float, theta1: float) -> None:
    with open(file, "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f, ident=4)

def main():
    pass

if __name__ == "__main__":
    main()
