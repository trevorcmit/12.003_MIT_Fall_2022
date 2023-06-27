import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main():
    phi, omegaT = np.linspace(0.0, np.pi, 100), np.linspace(-np.pi/2.0, np.pi/2.0, 100)
    phi, omegaT = np.meshgrid(phi, omegaT)
    insolation_map = insolation(phi, omegaT)
    plt.imshow(insolation_map, extent=[-np.pi/2.0, np.pi/2.0, 0.0, np.pi], origin='lower')
    plt.colorbar()
    plt.show()


def insolation(phi, omegaT):
    """
    """
    sin_del = -1.0 * np.sin(0.41) * np.cos(omegaT)
    cos_del = (1.0 - sin_del**2.0)**0.5
    h_0 = np.arccos(-1.0 * np.tan(phi) * sin_del)
    return 1360.0 / np.pi * (np.cos(phi) * cos_del * np.sin(h_0) + np.sin(phi) * sin_del * h_0)



graph = np.zeros((100, 100)) # Initialize array to represent heatmap
time, lat = np.linspace(0.0, 2.0 * np.pi, 100), np.linspace(-np.pi/2.0, np.pi/2.0, 100)
for j in range(100):
    for i in range(100):
        graph[j][i] = insolation(lat[j], time[i])




latitude = np.linspace(-np.pi /2.0, np.pi / 2.0, 100)
annual = np.zeros(100)

for i in range(100):
    count = 0
    for n in range(365):
        val = insolation(latitude[i], (2.0 * np.pi * float(n)) / 365.0)
        if not math.isnan(val):
            count += 1
            annual[i] += val

    annual[i] /= count

plt.plot(latitude, annual, color="#243aff")
plt.xlabel("Latitude", fontsize=16)
plt.ylabel("Annual Mean Insolation", fontsize=16)
plt.xticks(
    ticks=np.linspace(-np.pi /2.0, np.pi / 2.0, 19),
    labels=['-90°','-80°','-70°','-60°','-50°','-40°','-30°','-20°','-10°','0°','10°','20°','30°','40°','50°','60°','70°','80°','90°'],
    rotation=-45.0,
    fontsize=15
)
plt.grid()
plt.show()


# plt.figure(figsize = (10, 6))
# plt.imshow(graph, cmap='viridis', interpolation="nearest", aspect='auto')

# plt.axvline(x=0.0,  color='black')
# plt.axvline(x=25.0, color='black')
# plt.axvline(x=50.0, color='black')
# plt.axvline(x=74.0, color='black')
# plt.xticks(
#     ticks=[0, 25, 50, 74, 99],
#     labels=['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'],
#     fontsize=15
# )
# plt.yticks(
#     ticks=np.linspace(0.0, 100.0, 19),
#     labels=['-90°','-80°','-70°','-60°','-50°','-40°','-30°','-20°','-10°','0°','10°','20°','30°','40°','50°','60°','70°','80°','90°'],
#     fontsize=15
# )
# plt.axhline(y=50.0, color='#333')
# plt.gca().invert_yaxis()
# plt.colorbar()
# plt.title("Daily-mean Insolation", fontsize=15)
# plt.show()
