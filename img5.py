# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:21:50 2024

@author: owner
"""

import matplotlib.pyplot as plt

# Updated data for current density vs power density
current_density_power = [
    (0, 0),
    (808.823214270287, 651.9275429729496),
    (955.8824700880083, 787.9819506190347),
    (1264.7059648507104, 992.0635620881619),
    (1750.000028049241, 1303.855085945899),
    (2647.059199719239, 1836.7347627253357),
    (3176.4709050267256, 2103.1747308666486),
    (3470.58807029858, 2131.519226124124),
    (3750.0002524431725, 2148.5260270798844),
    (4999.999214621239, 1587.3015955397839),
    (5705.881488364557, 1145.1247706900078)
]

# Data for current density vs voltage remains the same
current_density_voltage = [
    (0, 900.2267331257794),
    (794.1182311430275, 843.5374312070024),
    (1000.0001121969658, 823.1292700600897),
    (1264.7059648507104, 800.4535700528339),
    (1735.2936985583922, 757.36960509739),
    (2691.176841828195, 691.6100439359659),
    (3161.7645755358767, 662.1315197451306),
    (3485.294399789429, 614.5124770690009),
    (3764.7052355704323, 580.4988751574797),
    (5029.411873602938, 317.46042290923225),
    (5705.881488364557, 197.27899488809865)
]

# Unpack the updated data into separate lists
cd_power, power_density = zip(*current_density_power)
cd_voltage, voltage = zip(*current_density_voltage)

# Create a figure and axis for plotting
fig, ax1 = plt.subplots()

# Plot current density vs voltage on left y-axis
line1, = ax1.plot(cd_voltage, voltage, 'b-o', label='Voltage')
ax1.set_xlabel('Current Density(mA/m²)')
ax1.set_ylabel('Voltage (mV)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Set the x-axis and y-axis limits to start from 0
ax1.set_xlim([0, 6000])
ax1.set_ylim([0, 1000])

# Create a second y-axis for power density
ax2 = ax1.twinx()
line2, = ax2.plot(cd_power, power_density, 'r-s', label='Power Density')
ax2.set_ylabel('Power Density(mW/m²)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the y-axis limits for power density to start from 0
ax2.set_ylim([0, 2500])

# Add title and grid
plt.title('(e)PWW (AFW)')

# Add legends below each other
lines = [line1, line2]
labels = [line1.get_label(), line2.get_label()]

# Create a single legend
fig.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=1)

# Add grid
ax1.grid(True)

# Save the figure with 300 DPI
plt.savefig('img5.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
