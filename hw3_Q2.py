import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def T_EBM(phi):
    """
    Calculates temp. as function of latitude of Earth using EBM Model
    """
    return 288.0 + (-30.0 * 0.5 * (3.0 * np.sin(phi)**2.0 - 1.0))

def T_Full(phi):
    # omega = 7.2921e-5
    # a = 6.4e6
    # coeff = -2.0 * omega**2 * a**2 / 9.8 / 12000.0
    # term1 = -1.0*coeff * np.log(np.cos(phi))
    # term2 = -1.0*coeff/2.0 * np.sin(phi)**2
    # return np.e ** (term1 + term2)

    omega = 7.2921e-5
    a = 6.4e6
    g = 9.8
    h = 12000.0
    T_e = 303.0

    coeff = -2.0 * omega**2.0 * a**2.0 / g / h
    integ = -1.0 * np.log(np.cos(phi)) + (np.cos(phi)**2.0)/2.0
    return 

lats = np.linspace(-np.pi / 2.0, np.pi / 2.0, 100)


plt.plot(lats, T_EBM(lats),  color="#243aff", label=r"$T_{EBM}$")
plt.legend() # plt.plot(lats, T_Full(lats), color="#ff2424")
plt.ylabel("T (Kelvin)")
plt.xticks(
    ticks=np.linspace(-np.pi / 2.0, np.pi / 2.0, 19),
    labels=['-90°','-80°','-70°','-60°','-50°','-40°','-30°','-20°','-10°','0°','10°','20°','30°','40°','50°','60°','70°','80°','90°'],
    fontsize=12,
    rotation=45
)
plt.show()