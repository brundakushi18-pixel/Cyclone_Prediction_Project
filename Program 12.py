# Program 12 – Visualization of a mini bar graph.

 # It visualizes a mini bar graph which represents parameters of the entered date, month and year.
import matplotlib.pyplot as plt
import numpy as np

# 📊 Visualize parameters of the selected date
if not sel.empty:
    params = sel.drop(columns=['Year', 'Month', 'Date', 'Cyclone']).iloc[0]

    # 🔹 Apply log scaling to handle large value differences
    log_values = np.log10(params + 1)  # +1 to avoid log(0)

    plt.figure(figsize=(7, 4))
    plt.bar(params.index, log_values, color='skyblue', edgecolor='black')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Log-scaled Value (log₁₀)")
    plt.title(f"Cyclone Parameters on {d:02d}-{m:02d}-{y}")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


