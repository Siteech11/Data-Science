import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.125
fig = plt.subplots(figsize=(12, 8))

# set height of bar
Air_Pollution = [2.3, 2.9, 1.6, 3.8, 0]
Alcohol_Use = [3.4, 1.3, 2.1, 4.5, 0]
Dust_Allergy = [3.4, 4, 3.3, 5.2, 0]
Occupational_Hazard = [4.2, 4.2, 3.8, 4.5, 0]
Genetic_Risk = [4.2, 3, 3.5, 4.4, 0]

# Set position of bar on X axis
br1 = np.arange(len(Air_Pollution))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]

# Make the plot
plt.bar(br1, Air_Pollution, color='r', width=barWidth,
        edgecolor='grey', label='Air Pollution')
plt.bar(br2, Alcohol_Use, color='g', width=barWidth,
        edgecolor='grey', label='Alcohol Use')
plt.bar(br3, Dust_Allergy, color='b', width=barWidth,
        edgecolor='grey', label='Dust Allergy')
plt.bar(br4, Occupational_Hazard, color='#FFD700', width=barWidth,
        edgecolor='grey', label='Occupational Hazard')
plt.bar(br5, Genetic_Risk, color='#FF83FA', width=barWidth,
        edgecolor='grey', label='Genetic Risk')

# Adding Xticks
plt.xlabel('Age Group', fontweight='bold', fontsize=15)
plt.ylabel('Severity', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Air_Pollution))],
           ['14-26', '27-39', '40-52', '53-65', '65-73'])

# displaying the title
plt.title("Female Graph 1", fontweight='bold', fontsize=25)

plt.legend()
plt.show()

