import matplotlib.pyplot as plt

# Data for current density vs voltage
current_density_voltage = [
    (0, 498.57147216796875),
    (561.151377662748, 507.1429007393973),
    (803.9571197313752, 492.8571428571429),
    (1014.3887628575187, 462.85714285714283),
    (1375.8992050555544, 437.1428571428571),
    (1602.5178976529403, 428.5714285714286),
    (2007.1941344339864, 372.8571428571428),
    (2336.330971679085, 315.7143075125557),
    (2465.82736744902, 304.2857142857143),
    (2627.6978621614376, 262.85718645368297),
    (2827.3383036366026, 128.57142857142856)
]

# Data for current density vs power density
current_density_power = [
    (0, 8.571428571428457),
    (588.1296287849683, 227.14285714285705),
    (787.7700702601334, 294.2857360839843),
    (1003.597067216993, 358.57145036969865),
    (1375.8992050555544, 452.85716465541293),
    (1613.309593293466, 520.0000435965402),
    (2007.1941344339864, 564.2857360839844),
    (2330.9351238588224, 554.2857578822544),
    (2455.036165798041, 552.8571428571428),
    (2660.0719611039212, 510),
    (2838.129505287581, 264.2857360839844)
]

current_density_power = [(cd, pd * 800/600) for cd, pd in current_density_power]

# Unpack data into separate lists
cd_voltage, voltage = zip(*current_density_voltage)
cd_power, power_density = zip(*current_density_power)

# Create a figure and axis for plotting
fig, ax1 = plt.subplots()

# Plot current density vs voltage on left y-axis
ax1.plot(cd_voltage, voltage, 'b-o', label='Voltage')
ax1.set_xlabel('Current Density(mA/m²)')
ax1.set_ylabel('Voltage (mV)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Set the x-axis limits to go from 0 to 3000
ax1.set_xlim([0, 3000])
# Set the y-axis limits for voltage
ax1.set_ylim([0, 600])

# Create a second y-axis for power density
ax2 = ax1.twinx()
ax2.plot(cd_power, power_density, 'r-s', label='Power Density')
ax2.set_ylabel('Power Density(mW/m²)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the y-axis limits for power density
ax2.set_ylim([0, 800])

# Add title and grid
plt.title('Current Density vs Voltage and Power Density')
ax1.grid(True)

# Save the figure with 300 DPI
plt.savefig('img1.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
