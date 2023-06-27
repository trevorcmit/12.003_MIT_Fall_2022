import numpy as np
import matplotlib.pyplot as plt
import sys



def h(phi, omegaT):
    num = np.tan(phi) * np.sin(0.41) * np.cos(omegaT)
    denom = np.sqrt(1.0 - np.sin(0.41)**2.0 * np.cos(omegaT)**2.0)
    return 2.0 * np.arccos(num/denom)


time, lat = np.linspace(0.0, 2.0*np.pi, 100), np.linspace(-np.pi/2.0, np.pi/2.0, 100)


graph = np.zeros((100, 100)) # Initialize array to represent heatmap
time, lat = np.linspace(0.0, 2.0 * np.pi, 100), np.linspace(-np.pi/2.0, np.pi/2.0, 100)
for j in range(100):
    for i in range(100):
        graph[j][i] = h(lat[j], time[i])

plt.imshow(graph, cmap='plasma', interpolation="nearest", aspect='auto')


plt.xticks(
    ticks=[0, 25, 50, 74, 99],
    labels=['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'],
    fontsize=15
)
plt.yticks(
    ticks=np.linspace(0.0, 100.0, 19),
    labels=['-90°','-80°','-70°','-60°','-50°','-40°','-30°','-20°','-10°','0°','10°','20°','30°','40°','50°','60°','70°','80°','90°'],
    fontsize=15
)
plt.axhline(y=50.0, color='#333')
plt.xlabel("Time (" + r'$\omega t$'+")", fontsize=16)
plt.title("Length of Day", fontsize=16)
plt.ylabel("Latitude", fontsize=16)
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()


# m = np.zeros((100, 100)) # Initialize array to represent heatmap
# for j in range(100):
#     for i in range(100):
#         m[i][j] = h(lat[i], time[j])

# time, lat = np.meshgrid(np.linspace(0.0, 2.0 * np.pi, 100), np.linspace(-np.pi/2.0, np.pi/2.0, 100))
# plt.imshow(m, cmap='viridis')
# plt.colorbar()
# plt.show()

# plt.figure()
# CS = plt.contour(time,lat,ccc, [1.0, 2.0, 3.0,4.0,5.0])
# plt.clabel(CS,inline=True, fontsize=10)
# plt.show()

# omega = 2 * np.pi / 365.0 * 24.0