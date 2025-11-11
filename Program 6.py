# Program 6 – Boxplot Visualization

# It draws boxplots comparing each parameter (temperature, pressure, humidity, etc.) between cyclone and non-cyclone days to see which factors affect cyclone formation.


features = ['Sea_Surface_Temperature_C', 'Atmospheric_Pressure_hPa', 'Humidity_pct', 'Wind_Shear_ms', 'Vorticity_s^-1', 'Ocean_Depth_m', 'Proximity_to_Coast_km', 'Pre_Existing_Disturbance'] 
plt.figure(figsize=(15,10))
 for i, col in enumerate(features, 1):
      plt.subplot(3, 3, i)
      sns.boxplot(x='Cyclone_Formation', y=col, data=df) 
plt.title(col) plt.tight_layout() 
plt.show()