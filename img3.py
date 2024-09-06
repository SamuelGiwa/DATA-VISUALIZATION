# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:56:25 2024

@author: owner
"""

import matplotlib.pyplot as plt

# New Data for current density vs power density
current_density_power = [
    (0, 0),
    (690.355431388783, 223.48182789644827),
    (1177.665038313887, 346.55871105627006),
    (1451.7766922092583, 365.9919070358082),
    (1695.4314956718108, 414.5748969846536),
    (2324.8727614602985, 502.02427889257535),
    (3543.146778773059, 672.0647437135342),
    (3543.146778773059, 672.0647437135342),
    (4182.740637862259, 694.7368304002486),
    (4507.61432879187, 660.7287374360567),
    (5005.075599548371, 527.9352562864659),
    (5167.512445013177, 309.31180151666155)
]

# New Data for current density vs voltage
current_density_voltage = [
    (0, 697.9757211074248),
    (690.355431388783, 649.3927311585794),
    (1157.3603164471222, 586.2348442250803),
    (1492.3861359427879, 497.16597989769076),
    (1725.8883461046298, 479.3522663376205),
    (2345.1779480617197, 434.00809296419175),
    (3532.9951149416615, 385.42510301534634),
    (4152.283787429439, 341.7004120613855),
    (4527.918585923978, 297.9757211074247),
    (5005.075599548371, 213.76522990667917),
    (5197.969295445996, 126.3158479987574)
]

current_density_power = [(cd, pd * 1600/800) for cd, pd in current_density_power]
# Unpack data into separate lists
cd_power, power_density = zip(*current_density_power)
cd_voltage, voltage = zip(*current_density_voltage)

# Create a figure and axis for plotting
fig, ax1 = plt.subplots()

# Plot current density vs voltage on left y-axis
line1, = ax1.plot(cd_voltage, voltage, 'b-o', label='Voltage')
ax1.set_xlabel('Current Density(mA/m²)')
ax1.set_ylabel('Voltage (mV)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Set the x-axis limits
ax1.set_xlim([0, 6000])
# Set the y-axis limits for voltage
ax1.set_ylim([0, 800])

# Create a second y-axis for power density
ax2 = ax1.twinx()
line2, = ax2.plot(cd_power, power_density, 'r-s', label='Power Density')
ax2.set_ylabel('Power Density(mW/m²)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the y-axis limits for power density
ax2.set_ylim([0, 1600])

# Add title and grid
plt.title('(c)PWW(OFW)')

# Add legends below each other
lines = [line1, line2]
labels = [line1.get_label(), line2.get_label()]

# Create a single legend
fig.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=1)

# Add grid
#ax1.grid(True)
ax2.grid(True)

# Save the figure with 300 DPI
plt.savefig('img3.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
