import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Monte Carlo Simulation to Estimate π")

# Introduction
st.write("""
This app uses a Monte Carlo simulation to estimate the value of π. 
The idea is to randomly generate points in a unit square and count how many fall within the quarter circle.
""")

# Input from the user: number of points for the simulation
n_points = st.slider("Number of points", min_value=1000, max_value=100000, step=1000, value=10000)

# Run the Monte Carlo simulation
x = np.random.rand(n_points)
y = np.random.rand(n_points)
distances = np.sqrt(x**2 + y**2)
inside_circle = distances <= 1
n_inside_circle = np.sum(inside_circle)

# Estimate of pi
pi_estimate = (n_inside_circle / n_points) * 4

# Display the result
st.write(f"Estimated value of π: {pi_estimate:.4f}")

# Plot the points inside and outside the quarter circle
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
ax.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
ax.set_aspect('equal', 'box')
ax.legend()
st.pyplot(fig)

# Footer
st.write("Increase the number of points using the slider above to improve the accuracy of the estimate.")
