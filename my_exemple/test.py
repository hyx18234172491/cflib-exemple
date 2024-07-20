import matplotlib.pyplot as plt
import pandas as pd

# Data
prices = [59.35, 59.75, 59.25, 59.05, 59.40, 59.10, 59.05, 58.90, 58.35, 58.15, 58.15, 58.20, 57.70, 57.65, 57.85, 57.60, 57.55]
dates = pd.date_range(start="2023-06-23", periods=len(prices), freq='D')

# Plotting the line chart
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, marker='o')
plt.title('Price from June 23')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
