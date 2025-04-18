import streamlit as st

# Constants
rho = 1000  # Density of water in kg/m³
g = 9.81    # Gravitational acceleration in m/s²

# Function to calculate micro-hydro power
def calculate_power(head, flow_rate, efficiency):
    power = rho * g * head * flow_rate * efficiency  # in Watts
    return power

# Set up Streamlit UI
st.title("Micro Hydro Power Calculator")

# Input fields
head = st.number_input("Enter Head (m):", min_value=1.0, value=10.0)
flow_rate = st.number_input("Enter Flow Rate (m³/s):", min_value=0.001, value=0.05)
efficiency = st.slider("Select Turbine Efficiency (%):", min_value=50, max_value=100, value=70) / 100

# Calculate power output
power_output = calculate_power(head, flow_rate, efficiency)

# Display results
st.write(f"Calculated Power Output: {power_output:.2f} Watts")

# Convert to kilowatts (optional for larger systems)
st.write(f"Power Output (in kW): {power_output / 1000:.2f} kW")

# Power generation per year (assuming 24/7 operation)
annual_power = power_output * 24 * 365  # in Watt-hours
st.write(f"Annual Power Generation: {annual_power / 1000:.2f} kWh/year")

# Energy savings (example: electricity cost savings)
electricity_cost_per_kwh = st.number_input("Enter the electricity cost per kWh (in your local currency):", min_value=0.01, value=0.12)
annual_savings = annual_power / 1000 * electricity_cost_per_kwh  # annual savings in local currency
st.write(f"Estimated Annual Savings: {annual_savings:.2f} (your local currency)")

# Optional: Plotting a bar chart of power output and annual savings
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(["Power Output (W)", "Annual Savings"], [power_output, annual_savings])
ax.set_ylabel("Value")
ax.set_title("Micro Hydro System Performance")
st.pyplot(fig)

# Additional Information
st.subheader("Important Notes:")
st.write("""
1. **Head (H)**: The vertical distance the water falls. The higher the head, the more power can be generated.
2. **Flow Rate (Q)**: The volume of water flowing through the system per second. A higher flow rate means more power.
3. **Efficiency (η)**: Not all the energy from water is converted into electricity. Turbines have an efficiency that ranges between 50% to 90%.
4. This tool assumes continuous operation for the calculation of annual power generation. Actual performance may vary based on seasonal changes in water flow and availability.
""")

# Downloadable Report
st.subheader("Download Your Report")
report_data = {
    "Head (m)": [head],
    "Flow Rate (m³/s)": [flow_rate],
    "Turbine Efficiency (%)": [efficiency * 100],
    "Power Output (W)": [power_output],
    "Annual Power Generation (kWh)": [annual_power / 1000],
    "Annual Savings": [annual_savings],
}

import pandas as pd
df = pd.DataFrame(report_data)
csv = df.to_csv(index=False)
st.download_button(
    label="Download Report as CSV",
    data=csv,
    file_name="micro_hydro_report.csv",
    mime="text/csv",
)
