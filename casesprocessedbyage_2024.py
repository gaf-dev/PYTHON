import pandas as pd
import matplotlib.pyplot as plt


ruta_csv = r'sneep-2019.csv'
df = pd.read_csv(ruta_csv)


print(df.columns)  


nombre_columna_edad = 'edad'  
if nombre_columna_edad in df.columns:
   
    df[nombre_columna_edad] = pd.to_numeric(df[nombre_columna_edad], errors='coerce')

    
    df = df.dropna(subset=[nombre_columna_edad])

    
    plt.figure(figsize=(10, 5))
    plt.hist(df[nombre_columna_edad], bins=20, color='blue', alpha=0.7)
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y')
    plt.show()

    
    plt.savefig(r'C:\Users\gabri\OneDrive\Escritorio\histograma_edades.png')
else:
    print(f"La columna '{nombre_columna_edad}' no existe en el DataFrame.")
