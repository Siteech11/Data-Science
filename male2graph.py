import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.125
fig = plt.subplots(figsize=(12, 8))

# set height of bar
Chronic_Lung_Disease = [4.2, 4.9, 4.4, 4.9, 5]
Balanced_Diet = [4.1, 5.7, 3.9, 4.5, 6]
Obesity = [4.1, 4.1, 4.4, 3.9, 5]
Smoking = [4, 4.1, 4.4, 4.5, 8]
Passive_Smoking = [4, 4.5, 5, 4, 5]

# Set position of bar on X axis
br1 = np.arange(len(Chronic_Lung_Disease))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]

# Make the plot
plt.bar(br1, Chronic_Lung_Disease, color='r', width=barWidth,
        edgecolor='grey', label='Chronic Lung Disease')
plt.bar(br2, Balanced_Diet, color='g', width=barWidth,
        edgecolor='grey', label='Balanced Diet')
plt.bar(br3, Obesity, color='b', width=barWidth,
        edgecolor='grey', label='Obesity')
plt.bar(br4, Smoking, color='#FFD700', width=barWidth,
        edgecolor='grey', label='Smoking')
plt.bar(br5, Passive_Smoking, color='#FF83FA', width=barWidth,
        edgecolor='grey', label='Passive Smoking')

# Adding Xticks
plt.xlabel('Age Group', fontweight='bold', fontsize=15)
plt.ylabel('Severity', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Chronic_Lung_Disease))],
           ['14-26', '27-39', '40-52', '53-65', '65-73'])

# displaying the title
plt.title("Male Graph 2", fontweight='bold', fontsize=25)

plt.legend()
plt.show()

