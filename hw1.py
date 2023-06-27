from cmath import nan
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gammainc, gamma
import math
import sys


# tau = np.linspace(start=0.0, stop=10.0, num=100) # Get tau_0 in the range 0 to 10

# def OLR_over_SBE(tau:float, b:float):
#     incomplete = math.e**(-tau) + tau**(-1.0*b) * gammainc(1.0+b, tau)
#     complete = gamma(b+1.0)
#     return incomplete * complete # Multiply by complete to de-normalize


# plt.plot(tau, [OLR_over_SBE(t, 0.5) for t in tau], color="#2bb5ff", label="b=0.5")
# plt.plot(tau, [OLR_over_SBE(t, 1.0) for t in tau], color="#053fb3", label="b=1.0")
# plt.plot(tau, [OLR_over_SBE(t, 1.5) for t in tau], color="#020335", label="b=1.5")
# plt.legend(loc="upper right")
# plt.xlabel(u'τ\u2080', fontsize=12)
# plt.ylabel("OLR/σ" + r'$T_s^4$', fontsize=12)
# plt.show()


# tau = np.linspace(start=0.0, stop=1.0, num=100) # Get tau_0 in the range 0 to 10

# def T_s(T_e, tau_0, b):
#     incomplete = math.e**(-tau_0) + tau_0**(-1.0*b) * gammainc(1.0+b, tau_0)
#     complete = gamma(b+1.0)
#     denom = incomplete * complete
#     return T_e / denom

# plt.plot(tau, [T_s(255.0, t, 0.3) for t in tau], color="#ffa1a1", label="n=0.5")
# plt.plot(tau, [T_s(255.0, t, 0.2) for t in tau], color="#eb0000", label="n=1.0")
# plt.plot(tau, [T_s(255.0, t, 0.1) for t in tau], color="#2a0000", label="n=1.5")
# plt.legend(loc="upper left")
# plt.title(r'$T_s$'+" vs. " + u'τ\u2080' + " for varying " + 'n' + ", "+ r'$T_s$' + "=255 K",fontsize=12)
# plt.xlabel(u'τ\u2080', fontsize=12)
# plt.ylabel(r'$T_s$'+" (Kelvin)", fontsize=12)
# plt.show()


lat = np.linspace(-np.pi/2.0, np.pi/2.0, 100)
lon = np.linspace(-np.pi, np.pi, 100)

def T_s(phi, theta):
    """
    Function to calculate T_s given lat/long on alt-rock star model
    """
    if np.cos(theta) > 0: # Check light side or dark side of moon
        return 0.0
    else:
        return (1360.0 * 0.9 * np.cos(phi) * abs(np.cos(theta))/4.0 / 5.67037e-8)**0.25

m = np.zeros((100, 100)) # Initialize array to represent heatmap
for i in range(100):
    for j in range(100):
        m[i][j] = T_s(lat[i], lon[j]) # lat = phi, lon = theta

plt.imshow(m, cmap='viridis') # Create heatmap plot
plt.xticks(
    ticks=[0, 24, 49, 74, 99],
    labels=[-180.0, -90.0, 0.0, 90.0, 180.0],
    fontsize=12
)
plt.yticks(
    ticks=[0, 24, 49, 74, 99],
    labels=[90.0, 45.0, 0.0, -45.0, -90.0],
    fontsize=12
)
plt.xlabel("Longitude", fontsize=12)
plt.ylabel("Latitute", fontsize=12)
plt.title("Theoretical Implementation of Alt-Rock Star Model", fontsize=12)
plt.colorbar()
plt.show()




