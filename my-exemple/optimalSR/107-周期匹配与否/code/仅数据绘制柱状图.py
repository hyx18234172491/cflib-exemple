# Data for bar chart
from matplotlib import pyplot as plt

x_label = [70, 60, 50, 40, 30, 20]
y_rangingRate_70msPeriod = [0.28, 0.43, 0.57, 0.71, 0.85, 1]
y_rangingRate_varPeriod = [1, 1, 0.99, 1, 0.99, 1]

# Width of the bars
bar_width = 2.8

# Adjusted bar chart code without grid and with value labels, improved legend placement
plt.figure(figsize=(8, 6))
bars1 = plt.bar([x - bar_width/2 for x in x_label], y_rangingRate_70msPeriod, width=bar_width, label='70 ms Period')
bars2 = plt.bar([x + bar_width/2 for x in x_label], y_rangingRate_varPeriod, width=bar_width, label='Variable Period')

# Adding value labels on top of each bar
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom')

# Customization
plt.xlabel('Period(ms)',fontsize=16)
plt.ylabel('Ranging Rate',fontsize=16)
# plt.title('Comparison of Ranging Rates for Different Periods')
plt.xticks(x_label)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=2)  # Legend placed at the top center

# Show plot
plt.show()
