import numpy as np
import matplotlib.pyplot as plt, random


# parameters
# name           value       units           comments
# --------------------------------------------------------------------------------------
A       =       -353;       # W/m^2         OLR intercept
B       =       2.00;       # W/m^2/K       OLR slope / radiative damping coefficient
D       =       3.8;        # W/m^2/K       climate heat transport coefficient; Roughly Budyko's \beta converted to SI
D_ref   =       3.8;        # W/m^2/K       reference value of heat transport coefficient
alpha_0 =       0.3;        # -             albedo when ice-free
alpha_2 =       0.1;        # -             second legendre polynomial coefficient for latitudinal dependence on albedo under ice-free conditions    
dalpha  =       0.22;       # -             increase in albedo when ice-covered
Tf      =       273.15;     # K             temperature threshold for ice
S0      =       1360;       # W/m^2         solar constant, perpendicular incidence
s2      =       -0.48;      # -             second legendre polynomial coefficient for insolation (normalized)  

yi      = np.linspace(0, 1, 1000)   # sine-latitude of ice edge
F_yi    = np.zeros(yi.shape)        # decrease in A required to maintain ice line at yi
ASR_yi  = np.zeros(yi.shape)        # solar absorption with ice-line at yi for reference S0
Tp_yi   = np.zeros(yi.shape)        # global-mean temperature with ice line at yi
Tp0_yi  = np.zeros(yi.shape)        # global-mean temperature with ice line at yi and F=0

insol   = S0/4 * (1 + s2 * 0.5 * (3 * yi**2 - 1))       # annual-mean insolation as a function of latitude
alpha_warm = alpha_0 + alpha_2 * 0.5 * (3 * yi**2 - 1)  # ice-free albedo
alpha_cold = alpha_warm + dalpha                        # ice-covered albedo 


# For each latitude, calculate ASR(y_i), F(y_i), and T_p(y_i)
for j in range(len(yi)):
    # Global-mean absorbed solar radiation with ice line at yi
    ASR_yi[j] =\
        yi[j] * np.mean(
            np.multiply(insol[:j+1], 1.0 - alpha_warm[:j+1]) # Below yi
        ) +\
        (1.0-yi[j]) * np.mean(
            np.multiply(insol[j:], 1.0-alpha_cold[j:])       # Above yi
        )

    Tp0_yi[j] = 1.0 / B * (ASR_yi[j] - A)
    num = -1.0 * ( insol[j] * ( 1.0-(alpha_warm[j] + alpha_cold[j])/2 ) - (A + B*Tf) + D*Tp0_yi[j]-Tf )
    denom = 1.0 + D/B

    # Radiative forcing required to keep partly ice-covered climate with ice line at yi
    F_yi[j] = num / denom

    # Global-mean temp. for partly ice-covered climate with ice line at yi
    Tp_yi[j] = 1 / B * (ASR_yi[j] - A + F_yi[j])


# Calc. min. possible radiative forcing that'll keep climate ice-free by setting polar T = Tf and using alpha_warm everywhere
F_min_icefree = -1.0*(insol[-1] * ( 1.0-alpha_warm[-1] ) - (A+B*Tf) + D*(Tp0_yi[-1]-Tf)) / (1+D/B)

# Calc. max possible solar forcing that allows snowball climate by setting equatorial T = Tf and using alpha_cold everywhere
F_max_snowball = -1.0*(insol[0] * ( 1.0-alpha_cold[0] ) - (A+B*Tf) + D*(Tp0_yi[0]-Tf)) / (1+D/B)

# Stability condition of the Budyko model is that the ice line retreat as the solar forcing increases, so filter calculations for that criterion
# Pad with leading negative value: model will always be unstable with the ice edge very close to equator
dyi_dlnS = np.array(np.diff(yi) / np.diff(F_yi))
dyi_dlnS = np.pad(dyi_dlnS, (1,0), 'constant', constant_values=(-1.0, -1.0))
