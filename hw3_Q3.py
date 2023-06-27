import numpy as np
import matplotlib.pyplot as plt
import sys
import math


f = 5.0e-5
tri = 500.0
L = 20000.0
g = 9.8


def V(r):
    coeff = f * r / 2.0
    num = 8.0 * g * tri
    denom = f**2.0 * L**2.0 * (1.0 + (r/L)**2.0)**2.0
    sqr = np.sqrt(1.0 + num/denom) - 1.0
    return coeff * sqr

def Ro(r):
    return V(r) / (f*r)

def V_g(r):
    numer = -2.0 * g * tri * r
    denom = f * L**2.0 * (1.0 + (r/L)**2.0)**2.0
    return numer / denom

def V_c(r):
    sqroot = ((-2.0 * g * tri) / (1.0 + (r/L)**2.0)**2.0)**0.5
    return (r/L) * sqroot


r_vals = np.linspace(0.01, 4.0e4, 500)


plt.plot(r_vals, V(r_vals),   color="#d1010e", label=r"$V(r)$")
# plt.plot(r_vals, Ro(r_vals),  color="#243aff", label="Ro" + r"$(r)$")
plt.xlabel(r"$r$" + " (meters)", fontsize=14)
# plt.yscale('log')
plt.plot(r_vals, V_g(r_vals), color="#01d102", label=r"$V_g(r)$")
# plt.plot(r_vals, V_c(r_vals), color="#cfb004", label=r"$V_c(r)$")
plt.legend()
plt.show()

