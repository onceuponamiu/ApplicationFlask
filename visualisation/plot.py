import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Charger les données CSV dans un DataFrame
df = pd.read_csv('pred-mai-mef-dhup-3.csv', delimiter=';', encoding='ISO-8859-1')

# Remplacer les virgules décimales françaises par des points pour convertir en flottant
df['loypredm2'] = df['loypredm2'].str.replace(',', '.').astype(float)

# Regrouper par département et calculer le prix moyen du loyer
avg_rent_by_dep = df.groupby('DEP')['loypredm2'].mean().reset_index()

# Normaliser les prix moyens des loyers pour la cartographie des couleurs
max_rent = avg_rent_by_dep['loypredm2'].max()
min_rent = avg_rent_by_dep['loypredm2'].min()
avg_rent_by_dep['normalized'] = (avg_rent_by_dep['loypredm2'] - min_rent) / (max_rent - min_rent)

# Charger le fichier GeoJSON pour les départements français
gdf_departments = gpd.read_file('departements-version-simplifiee.geojson')

# Fusionner les données de loyer moyen avec le GeoDataFrame
gdf_departments['DEP'] = gdf_departments['code']
gdf_map = gdf_departments.merge(avg_rent_by_dep, on='DEP', how='left')

# Créer une carte de couleur
cmap = 'OrRd'

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

# Tracer les données fusionnées, en utilisant la colonne 'normalized' pour la couleur et en ajoutant une légende
gdf_map.plot(column='normalized', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, cax=cax)

# Supprimer les axes
ax.axis('off')

# Définir le titre
ax.set_title('Prix Moyen des Loyers par Département en France', fontdict={'fontsize': '15', 'fontweight' : '3'})

# Afficher le tracé
plt.show()
