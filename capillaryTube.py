import math
import numpy as np
import matplotlib.pyplot as plt

# CAPILLARY RISE CALCULATION
def capillary_rise():
    print("\n--- Capillary Rise in a Tube ---")

    # User inputs
    gamma = float(input("Enter surface tension (N/m) [e.g., 0.0728 for water]: "))
    theta_deg = float(input("Enter contact angle in degrees [0 for water-glass]: "))
    rho = float(input("Enter density of liquid (kg/m^3) [e.g., 1000 for water]: "))
    g = float(input("Enter acceleration due to gravity (m/s²) [default 9.81]: "))
    r = float(input("Enter inner radius of the tube (m) [e.g., 0.001 for 1mm]: "))

    theta = math.radians(theta_deg)

    # Define the function and derivative
    def f(h):
        return h - (2 * gamma * math.cos(theta)) / (rho * g * r)

    def f_prime(h):
        return 1  # Since the rest are constants

    # Newton-Raphson Method
    def newton_raphson(h0=0.05, tolerance=1e-6, max_iter=100):
        for i in range(max_iter):
            h1 = h0 - f(h0) / f_prime(h0)
            if abs(h1 - h0) < tolerance:
                return h1
            h0 = h1
        raise Exception("Newton-Raphson did not converge")

    # Calculate height for user-provided radius
    h_actual = newton_raphson()
    print(f"\nCapillary rise height for radius {r*1000:.2f} mm: {h_actual*100:.2f} cm")

    # Graph: Varying radius vs height
    radii = np.linspace(0.0001, 0.005, 100)  # Radius from 0.1mm to 5mm
    heights = (2 * gamma * np.cos(theta)) / (rho * g * radii)

    plt.plot(radii * 1000, heights * 100, color='green', label='Capillary Rise Curve')
    plt.scatter([r * 1000], [h_actual * 100], color='red', label='Your Input')
    plt.xlabel("Tube Radius (mm)")
    plt.ylabel("Capillary Rise Height (cm)")
    plt.title("Capillary Rise vs Tube Radius")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# main call
if __name__ == "__main__":
    capillary_rise()
