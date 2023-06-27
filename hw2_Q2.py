import numpy as np
import matplotlib.pyplot as plt
import sys


# Rockport, Maine - Elevation: 687 feet, Latitude: 44 12N, Longitude: 069 09W
Rockport = [-6.8, -5.4, -0.6, 5.6, 11.6, 16.3, 19.5, 19.2, 14.9, 8.8, 3.5, -3.1]

# Rio de Los Ciervos, Chile - Elevation: 1 meter, Latitude: 53 08S, Longitude: 070 53W
RdlC = [11.0, 10.0, 9.0, 6.0, 3.0, 2.0, 1.0, 2.0, 4.0, 6.0, 8.0, 9.0]

# Sapporo, Japan - Elevation: 10 meters, Latitude: 43 07N, Longitude: 141 23E
Sapporo = [-3.6, -3.1, 0.6, 7.1, 12.4, 16.7, 20.5, 22.3, 18.1, 11.8, 4.9, -0.9]

# Rovaniemi, Finland - Elevation: 101 meters, Latitude: 66 30N, Longitude: 025 43E
Rovaniemi = [-11.8, -11.1, -6.1, -0.9, 6, 12.4, 15.2, 12.3, 6.9, 0.3, -6.1, -10.1]

# Marion Island, South Africa - Elevation: 21 meters, Latitude: 46 53S, Longitude: 037 52E
Marion = [7.0, 8.0,	7.0, 6.0, 5.0, 5.0, 4.0, 3.0, 4.0, 5.0, 6.0, 7.0]


# plt.plot(Rockport,  color="#2b7cff", marker=".", label="Rockport")
# plt.plot(RdlC    ,  color="#ebb400", marker=".", label="Rio de Los Ciervos")
# plt.plot(Sapporo,   color="#ff141c", marker=".", label="Sapporo")
# plt.plot(Rovaniemi, color="#ed37fa", marker=".", label="Rovaniemi")
# plt.plot(Marion,    color="#00d64f", marker=".", label="Marion")
# plt.ylabel("Month Avg. Temperature (°C)")
# plt.legend()
# plt.xticks(ticks=range(12), labels=["Jan","Feb",'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
# plt.show()


def a(temps):
    Sigma = 0
    for j in range(12):
        Sigma += temps[j] * np.cos(2.0 * np.pi * j / 12.0)
    return Sigma * 2.0 / 12.0

def b(temps):
    Sigma = 0
    for j in range(12):
        Sigma += temps[j] * np.sin(2.0 * np.pi * j / 12.0)
    return Sigma * 2.0 / 12.0


x = np.linspace(0.0, 11.0, 200)

sRockport, aRockport, bRockport = sum(Rockport)/12.0, a(Rockport), b(Rockport)
Rockport_fit = [sRockport + aRockport * np.cos(2.0*np.pi*j/12.0) + bRockport * np.sin(2.0*np.pi*j/12.0) for j in x]
sRdlC, aRdlC, bRdlC = sum(RdlC)/12.0, a(RdlC), b(RdlC)
RdlC_fit = [sRdlC + aRdlC * np.cos(2.0*np.pi*j/12.0) + bRdlC * np.sin(2.0*np.pi*j/12.0) for j in x]
sSapporo, aSapporo, bSapporo= sum(Sapporo)/12.0, a(Sapporo), b(Sapporo)
Sapporo_fit = [sSapporo + aSapporo * np.cos(2.0*np.pi*j/12.0) + bSapporo * np.sin(2.0*np.pi*j/12.0) for j in x]
sRovaniemi, aRovaniemi, bRovaniemi= sum(Rovaniemi)/12.0, a(Rovaniemi), b(Rovaniemi)
Rovaniemi_fit=[sRovaniemi+aRovaniemi* np.cos(2.0*np.pi*j/12.0)+bRovaniemi* np.sin(2.0*np.pi*j/12.0) for j in x]
sMarion, aMarion, bMarion = sum(Marion)/12.0, a(Marion), b(Marion)
Marion_fit=[sMarion+aMarion* np.cos(2.0*np.pi*j/12.0)+bMarion * np.sin(2.0*np.pi*j/12.0) for j in x]







x = np.linspace(0.0, 11.0, 12)
Rockport_fit = [sRockport + aRockport * np.cos(2.0*np.pi*j/12.0) + bRockport * np.sin(2.0*np.pi*j/12.0) for j in x]
RdlC_fit     = [sRdlC + aRdlC * np.cos(2.0*np.pi*j/12.0) + bRdlC * np.sin(2.0*np.pi*j/12.0) for j in x]
Sapporo_fit  = [sSapporo + aSapporo * np.cos(2.0*np.pi*j/12.0) + bSapporo * np.sin(2.0*np.pi*j/12.0) for j in x]
Rovaniemi_fit= [sRovaniemi+aRovaniemi* np.cos(2.0*np.pi*j/12.0)+bRovaniemi* np.sin(2.0*np.pi*j/12.0) for j in x]
Marion_fit   = [sMarion+aMarion* np.cos(2.0*np.pi*j/12.0)+bMarion * np.sin(2.0*np.pi*j/12.0) for j in x]

# fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2, 3, sharey=True, sharex=True)
# ax1.plot(x, Rockport_fit, color="#080075", label="Fitted")
# ax1.plot(Rockport,        color="#369eff", label="Rockport", marker=".")
# ax2.plot(x, RdlC_fit, color="#523800", label="Fitted")
# ax2.plot(RdlC,        color="#ffc64d", label="Rio de Los Ciervos", marker=".")
# ax3.plot(x, Sapporo_fit, color="#700e0a", label="Fitted")
# ax3.plot(Sapporo,        color="#ff6661", label="Sapporo", marker=".")
# ax4.plot(x, Rovaniemi_fit, color="#610061", label="Fitted")
# ax4.plot(Rovaniemi,        color="#ff69ff", label="Rovaniemi", marker=".")
# ax5.plot(x, Marion_fit, color="#03420f", label="Fitted")
# ax5.plot(Marion,        color="#2eff54", label="Rovaniemi", marker=".")


correlation_matrix = np.corrcoef(Rockport, Rockport_fit)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(r_squared)

correlation_matrix = np.corrcoef(RdlC, RdlC_fit)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(r_squared)

correlation_matrix = np.corrcoef(Sapporo, Sapporo_fit)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(r_squared)

correlation_matrix = np.corrcoef(Marion, Marion_fit)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2.0
print(r_squared)

correlation_matrix = np.corrcoef(Rovaniemi, Rovaniemi_fit)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(r_squared)

plt.plot(x, Rockport_fit, color="#080075", marker=".")
plt.plot(x, Rockport,        color="#369eff", label="Rockport (0.996)", marker=".")
plt.plot(x, RdlC_fit, color="#523800", marker=".")
plt.plot(x,RdlC,        color="#ffc64d", label="Rio de Los Ciervos (0.983)", marker=".")
plt.plot(x, Sapporo_fit, color="#700e0a", marker=".")
plt.plot(x,Sapporo,        color="#ff6661", label="Sapporo (0.993)", marker=".")
plt.plot(x, Rovaniemi_fit, color="#610061", marker=".")
plt.plot(x,Rovaniemi,        color="#ff69ff", label="Rovaniemi (0.938)", marker=".")
plt.plot(x, Marion_fit, color="#03420f", marker=".")
plt.plot(x,Marion,        color="#2eff54", label="Marion (0.994)", marker=".")
plt.ylabel("Month Avg. Temperature (°C)")
plt.legend()
plt.xticks(ticks=range(0,12), labels=["Jan","Feb",'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.show();


jx_Rockport = 12.0/(2.0*np.pi) * (np.arctan(bRockport/aRockport) + np.pi)
jx_RdlC = 12.0/(2.0*np.pi) * (np.arctan(bRdlC/aRdlC))
jx_Marion = 12.0/(2.0*np.pi) * (np.arctan(bMarion/aMarion))
jx_Sapporo = 12.0/2.0/np.pi *(np.arctan(bSapporo/aSapporo) + np.pi)
jx_Rovaniemi = 12.0/2.0/np.pi *(np.arctan(bRovaniemi/aRovaniemi) + np.pi)

# print(jx_Rockport)
# print(jx_RdlC)
# print(jx_Marion)
# print(jx_Sapporo)
# print(jx_Rovaniemi)

# print(np.sqrt(aRockport**2 + bRockport**2))
# print(np.sqrt(aRdlC**2 + bRdlC**2))
# print(np.sqrt(aMarion**2 + bMarion**2))
# print(np.sqrt(aSapporo**2 + bSapporo**2))
# print(np.sqrt(aRovaniemi**2 + bRovaniemi**2))


# print(jx_Sapporo)