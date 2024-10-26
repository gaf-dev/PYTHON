import pandas as pd
file_path = '/mnt/data/Siembras_de__rboles_en_la_jurisdicci_n_de_Corantioquia_20240925.csv'
data = pd.read_csv(file_path)

# Columnas
data.head(), data.columns
# Filtrado
filtered_data = data[data['total hectareas'] > 100]
grouped_data = filtered_data.groupby(['nombre cientifico', 'municipio'])['arboles'].sum().reset_index()
sorted_data = grouped_data.sort_values(by=['nombre cientifico', 'arboles'], ascending=[True, False])
output_path = '/mnt/data/total_arboles_por_especie_y_municipio.csv'
sorted_data.to_csv(output_path, index=False)

output_path
