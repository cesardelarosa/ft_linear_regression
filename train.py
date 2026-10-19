import math
import sys

from utils import predict_price, read_csv, save_params


def normalize(values: list[float]) -> tuple[list[float], float, float]:
    v_min = min(values)
    v_max = max(values)
    delta = v_max - v_min
    if delta == 0:
        raise ValueError("Cannot normalize data: all values are identical.")
    v_norm = [(v - v_min) / delta for v in values]
    return v_norm, v_min, v_max


def gradient_descent(
    x: list[float], y: list[float], alpha: float, epochs: int, eps: float
) -> tuple[float, float]:
    theta0 = 0.0
    theta1 = 0.0
    m = len(x)

    for _ in range(epochs):
        errors = [predict_price(xi, theta0, theta1) - yi for xi, yi in zip(x, y)]

        d_theta0 = sum(errors) / m
        d_theta1 = sum(err * xi for err, xi in zip(errors, x)) / m

        if math.sqrt(d_theta0**2 + d_theta1**2) < eps:
            break

        theta0 -= alpha * d_theta0
        theta1 -= alpha * d_theta1

    return theta0, theta1


def denormalize(
    theta0_norm: float,
    theta1_norm: float,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
) -> tuple[float, float]:
    delta_x = x_max - x_min
    delta_y = y_max - y_min
    theta1 = theta1_norm * (delta_y / delta_x)
    theta0 = y_min + delta_y * theta0_norm - theta1 * x_min
    return theta0, theta1


def main():
    try:
        x, y = read_csv()
        x_norm, x_min, x_max = normalize(x)
        y_norm, y_min, y_max = normalize(y)
        theta0_norm, theta1_norm = gradient_descent(
            x_norm, y_norm, alpha=0.1, epochs=2500, eps=1e-6
        )
        theta0, theta1 = denormalize(
            theta0_norm, theta1_norm, x_min, x_max, y_min, y_max
        )
        save_params(theta0, theta1)

    except (ValueError, OSError) as e:
        sys.exit(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
