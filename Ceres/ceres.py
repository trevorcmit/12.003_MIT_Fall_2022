import netCDF4
import matplotlib.pyplot as plt
import numpy as np



# Read in data from netCDF file
data = netCDF4.Dataset('CERES_EBAF-TOA_Ed4.0_Subset_CLIM01-CLIM12.nc')

# NetCDF global attributes
nc_attrs = data.ncattrs()

# Dimension shape information.
nc_dims = [dim for dim in data.dimensions]  # list of nc dimensions

# Variable information.
nc_vars = [var for var in data.variables]  # list of nc variables


lats = data.variables['lat'][:]
sw_reflected = np.array(data.variables['ztoa_sw_all_clim'][:])
insolation   = np.array(data.variables['zsolar_clim'][:])

print(lats.shape)


annual_insolation = np.mean(a=insolation, axis=0)
annual_asr = np.mean(a=insolation - sw_reflected, axis=0)


annual_albedo = 1.0 - (annual_asr/annual_insolation)

fit, (ax1, ax2)= plt.subplots(2, 1, sharex=True)

ax1.plot(lats, annual_insolation, color='#1787ff', label="Insolation")
ax1.plot(lats, annual_asr, color="#fa0043", label="Annual ASR")
ax1.legend(loc="lower center")
ax1.set_ylabel("W"+r'$\cdot$'+"m"+r'$^{-2}$', fontsize=16)
ax2.set_ylabel("Albedo", fontsize=16)

ax2.plot(lats, annual_albedo, color="#109554")
plt.show()
# print(annual_albedo)
