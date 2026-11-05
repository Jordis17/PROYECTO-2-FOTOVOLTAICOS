# -*- coding: utf-8 -*-

!pip install pvlib
!pip install nrel-pysam

import pvlib

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

# latitude, longitude, name, altitude, timezone
latitude, longitude, name, altitude, timezone = 9.376950, -83.701886, 'CoopeAgri Perez Zeledon', 704, 'America/Costa_Rica'

# get the module and inverter specifications from SAM (version actualizada en GitHub)
url_modules = "https://raw.githubusercontent.com/NREL/SAM/refs/heads/develop/deploy/libraries/CEC%20Modules.csv"
url_inverters = "https://raw.githubusercontent.com/NREL/SAM/refs/heads/develop/deploy/libraries/CEC%20Inverters.csv"

cec_modules = pvlib.pvsystem.retrieve_sam(path=url_modules)

cec_inverters = pvlib.pvsystem.retrieve_sam(path=url_inverters)

cec_modules

cec_modules.columns[cec_modules.columns.str.contains('AIKO', case=False)]

cec_inverters.columns[cec_inverters.columns.str.contains('SCA25KTL', case=False)]

module = cec_modules['AEG_SOLAR_ENERGY_SRL_ALPS54D30_450_TP']

inverter = cec_inverters['Chint_Power_Systems_America__CPS_SCA25KTL_DO_US_208_{208V}']

temperature_model_parameters = pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_polymer']

module

inverter

temperature_model_parameters

# parametros del modelo de un diodo del AIKO-A450-MAH54Mb a partir de su hoja de datos
I_L_ref, I_o_ref, R_s, R_sh_ref, a_ref, Adjust = pvlib.ivtools.sdm.fit_cec_sam(
    'monoSi', v_mp=33.70, i_mp=13.36, v_oc=40.69, i_sc=14.12,
    alpha_sc=0.0005 * 14.12, beta_voc=-0.0022 * 40.69, gamma_pmp=-0.26,
    cells_in_series=54)

my_new_module = module.copy()
my_new_module["Manufacturer"] = "AIKO"
my_new_module["STC"] = 450.0
my_new_module["A_c"] = 1.992
my_new_module["Length"] = 1.757
my_new_module["Width"] = 1.134
my_new_module["N_s"] = 54
my_new_module["I_sc_ref"] = 14.12
my_new_module["V_oc_ref"] = 40.69
my_new_module["I_mp_ref"] = 13.36
my_new_module["V_mp_ref"] = 33.70
my_new_module["alpha_sc"] = 0.0005 * 14.12
my_new_module["beta_oc"] = -0.0022 * 40.69
my_new_module["gamma_pmp"] = -0.26
my_new_module["T_NOCT"] = 47
my_new_module["a_ref"] = a_ref
my_new_module["I_L_ref"] = I_L_ref
my_new_module["I_o_ref"] = I_o_ref
my_new_module["R_s"] = R_s
my_new_module["R_sh_ref"] = R_sh_ref
my_new_module["Adjust"] = Adjust
my_new_module.name = "AIKO-A450-MAH54Mb"
my_new_module

check = pvlib.pvsystem.singlediode(*pvlib.pvsystem.calcparams_cec(
    np.array([1000.0, 1000.0]), np.array([25.0, 65.0]),
    my_new_module['alpha_sc'], my_new_module['a_ref'], my_new_module['I_L_ref'],
    my_new_module['I_o_ref'], my_new_module['R_sh_ref'], my_new_module['R_s'],
    my_new_module['Adjust']))
pd.DataFrame(check).set_axis(['25 C', '65 C'])

# generacion mensual del proyecto (kWh) y HSP a 10 grados
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']

days = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

project = pd.Series([20092.5, 20066.2, 22394.7, 19094.3, 17261.6, 16378.4,
                     16613.2, 17637.5, 18305.2, 17558.5, 15827.0, 18296.1], index=months)

project_hsp = pd.Series([4.787, 5.300, 5.354, 4.723, 4.128, 4.043,
                         3.966, 4.211, 4.514, 4.187, 3.898, 4.360], index=months)

weather = pvlib.iotools.get_pvgis_tmy(latitude, longitude, map_variables=True)[0]
weather.index.name = 'utc_time'

weather

system = {'module': my_new_module, 'inverter': inverter,
          'surface_azimuth': 180, 'surface_tilt': 10, 'albedo': 0.12,
          'modules_per_string': 17, 'strings_per_inverter': [5, 5, 4, 4, 4]}

# perdidas del factor de rendimiento del proyecto que no calcula el modelo
soiling = 0.03
dc_losses = (1 - 0.02) * (1 - 0.02) * (1 - 0.01)

solpos = pvlib.solarposition.get_solarposition(
    time=weather.index,
    latitude=latitude,
    longitude=longitude,
    altitude=altitude,
    temperature=weather["temp_air"],
    pressure=pvlib.atmosphere.alt2pres(altitude),
)
dni_extra = pvlib.irradiance.get_extra_radiation(weather.index)
aoi = pvlib.irradiance.aoi(
    system['surface_tilt'],
    system['surface_azimuth'],
    solpos["apparent_zenith"],
    solpos["azimuth"],
)
total_irradiance = pvlib.irradiance.get_total_irradiance(
    system['surface_tilt'],
    system['surface_azimuth'],
    solpos['apparent_zenith'],
    solpos['azimuth'],
    weather['dni'],
    weather['ghi'],
    weather['dhi'],
    dni_extra=dni_extra,
    albedo=system['albedo'],
    model='haydavies',
)
cell_temperature = pvlib.temperature.sapm_cell(
    total_irradiance['poa_global'],
    weather["temp_air"],
    weather["wind_speed"],
    **temperature_model_parameters,
)
iam_diffuse = pvlib.iam.marion_diffuse('physical', system['surface_tilt'])
effective_irradiance = (total_irradiance['poa_direct'] * pvlib.iam.physical(aoi)
                        + total_irradiance['poa_sky_diffuse'] * iam_diffuse['sky']
                        + total_irradiance['poa_ground_diffuse'] * iam_diffuse['ground']) * (1 - soiling)
with np.errstate(divide='ignore', invalid='ignore'):
    dc = pvlib.pvsystem.singlediode(*pvlib.pvsystem.calcparams_cec(
        effective_irradiance, cell_temperature,
        my_new_module['alpha_sc'], my_new_module['a_ref'], my_new_module['I_L_ref'],
        my_new_module['I_o_ref'], my_new_module['R_sh_ref'], my_new_module['R_s'],
        my_new_module['Adjust']))
dc = dc.fillna(0).clip(lower=0)
ac = 0
for n_strings in system['strings_per_inverter']:
    v_dc = system['modules_per_string'] * dc['v_mp']
    p_dc = n_strings * system['modules_per_string'] * dc['p_mp'] * dc_losses
    ac = ac + pvlib.inverter.sandia(v_dc, p_dc, inverter).clip(lower=0)

solpos

total_irradiance

dc

ac

ac_local = ac.tz_convert(timezone)
poa_local = total_irradiance['poa_global'].tz_convert(timezone)

comparison = pd.DataFrame({
    'Proyecto': project,
    'PVLib PVGIS': (ac_local.groupby(ac_local.index.month).sum() / 1000).values,
})
comparison.loc['Total'] = comparison.sum()
comparison['Diferencia (%)'] = 100 * (comparison['PVLib PVGIS'] / comparison['Proyecto'] - 1)
comparison.round(1)

hsp = pd.DataFrame({
    'Proyecto': project_hsp,
    'PVLib PVGIS': (poa_local.groupby(poa_local.index.month).sum() / 1000).values / days,
})
hsp.round(2)

comparison.loc[months, ['Proyecto', 'PVLib PVGIS']].plot(kind='bar', rot=0, figsize=(12, 6))
plt.ylabel('Generacion mensual (kWh)')
plt.title('Generacion mensual del sistema de 168.3 kWp: proyecto vs PVLib (PVGIS)')
plt.savefig('comparacion_generacion_mensual.png', dpi=200, bbox_inches='tight')
comparison.to_csv('comparacion_generacion_mensual.csv')
