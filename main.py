import matplotlib.pyplot as plt
from physics import current_amps, p_loss, t_resistance

losses = []
voltages = [50_000, 150_000, 250_000, 350_000, 450_000]
r_perkm = 0.05 # ohms per km
l_km = 100 # km
power = 100_000_000 # 100 MW delivered

for v in voltages:
    i = current_amps(power, v)
    r_total = t_resistance(r_perkm, l_km)
    losses.append(p_loss(i,r_total))

plt.title("Transmission Power Loss vs. Voltage")
# Plot of power loss vs voltage at fixed distance (100km)
plt.plot([v/1000 for v in voltages], losses)
# Transmission voltages are written in kV.
plt.xlabel("Voltage (kV)")
plt.ylabel("Power loss (W)")
plt.yscale("log")
plt.show()

distances = [50, 150, 300, 450, 600]

for v in voltages:
    power_losses = []
    for d in distances:
       i = current_amps(power,v)
       r_total = t_resistance(r_perkm, d)
       power_losses.append(p_loss(i,r_total)) # Adds the power loss for each distance into power_losses
    plt.plot(distances,power_losses, label=f"{v/1000:.0f} kV")   # x = Distance (km) y = Power loss (W)

plt.title("Transmission Power Loss vs. Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Power loss (W)")
plt.yscale("log")
plt.legend()
plt.show()
