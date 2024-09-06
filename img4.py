import matplotlib.pyplot as plt

# New Data for current density vs power density
current_density_power = [
    (0, 0),
    (640.9862416268569, 214.1987524500339),
    (912.1725005908961, 296.9573942716771),
    (1146.379353771694, 365.1115731666541),
    (1583.9754779733496, 462.4746222033587),
    (1824.345283316573, 491.6835759124935),
    (2163.328530223794, 509.9391545708262),
    (2483.8212278350506, 505.07099097667),
    (2724.191033178274, 516.0243381716696),
    (3081.664265111897, 479.51318085500424),
    (3408.3204791551407, 433.26569635002636),
    (3778.1201796831774, 296.9573942716771),
    (5707.242703130517, -152.1298964349123)
]

current_density_power = [(cd, pd * 1.5) for cd, pd in current_density_power]

# New Data for current density vs voltage
current_density_voltage = [
    (0, 519.6754539033361),
    (640.9862416268569, 524.5436174974924),
    (912.1725005908961, 507.5050867016493),
    (1152.5423059341197, 495.33469164416),
    (1812.0188147221597, 424.74644488000604),
    (2163.328530223794, 367.5456131800287),
    (2477.658275672625, 320.08110866836364),
    (2724.191033178274, 292.0892585333233),
    (3093.9907337063105, 242.19065829667898),
    (3408.3204791551407, 202.028385248347),
    (3759.6301946567755, 127.78905060832889)
]

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
ax1.set_xlim([0, 4000])
# Set the y-axis limits for voltage to start from 0
ax1.set_ylim([0, 600])

# Create a second y-axis for power density
ax2 = ax1.twinx()
line2, = ax2.plot(cd_power, power_density, 'r-s', label='Power Density')
ax2.set_ylabel('Power Density(mW/m²)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Set the y-axis limits for power density to start from 0
ax2.set_ylim([0, 900])

# Add title and grid
plt.title('(d)PWW (MFW)')

# Add legends below each other
lines = [line1, line2]
labels = [line1.get_label(), line2.get_label()]

# Create a single legend
fig.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=1)

# Add grid
ax1.grid(True)

# Save the figure with 300 DPI
plt.savefig('img4.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
