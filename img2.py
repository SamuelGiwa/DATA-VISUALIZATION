import matplotlib.pyplot as plt

# Data for current density vs power density
current_density_power = [
    (787.0239435570319, 257.210373033023),
    (33.850363066621405, 0),
    (1159.3790994542862, 376.3593092032358),
    (1354.019558710674, 429.31444966201246),
    (1489.4213983652994, 467.13945104720744),
    (2377.996818510335, 695.9811163286791),
    (3165.0207620673664, 716.7848411181295),
    (3562.7645618879023, 701.6548751939273),
    (4425.952112885937, 656.2648042719416),
    (5009.873103266959, 482.2695035460993),
    (5238.36392558997, 247.7541659740692)
]

# Data for current density vs voltage
current_density_voltage = [
    (0, 758.3924638464096),
    (787.0239435570319, 754.6099290780141),
    (1150.9166055346661, 745.1536787317154),
    (1328.6316895636728, 722.4585999833777),
    (1489.4213983652994, 724.3499106549202),
    (2361.071830671094, 661.9385631371897),
    (3173.483643375127, 508.74707377548754),
    (3571.226668419383, 440.66196739250887),
    (4451.339982032938, 332.8605489527926),
    (5026.798091106201, 209.92907801418434),
    (5246.826032121449, 107.80141843971633)
]
current_density_power = [(cd, pd * 1800/800) for cd, pd in current_density_power]
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
ax2.set_ylabel('Power Density (W/cm²)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the y-axis limits for power density
ax2.set_ylim([0, 1800])

# Add title and grid
plt.title('(b)PWW (PFW)')

# Add legends below each other
lines = [line1, line2]
labels = [line1.get_label(), line2.get_label()]

# Create a single legend
fig.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=1)

# Add grid
ax1.grid(True)

# Save the figure with 300 DPI
plt.savefig('img2.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
