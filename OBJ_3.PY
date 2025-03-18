import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('INCENDIOS_FDA.sqlite')
print("Conexión a la base de datos exitosa.")

consulta_sql = """
    SELECT State, FIRE_YEAR, AVG(FIRE_SIZE) AS Promedio_Acres
    FROM Fires
    WHERE State IN (SELECT State FROM Fires GROUP BY State ORDER BY State )
    GROUP BY State, FIRE_YEAR
    ORDER BY State, FIRE_YEAR;
"""

df = pd.read_sql(consulta_sql, conn)

print(df)

conn.close()

estado_especifico = 'AZ'  
df_estado = df[df['STATE'] == estado_especifico]


if not df_estado.empty:
   
    df_estado['Promedio_Acres'] = df_estado['Promedio_Acres'].round(2)

   
    plt.figure(figsize=(12, 6))
    plt.bar(df_estado['FIRE_YEAR'].astype(str), df_estado['Promedio_Acres'], color='#0F1185')  

   
    plt.title(f'Promedio de Acres Quemados en Arizona por Año')
    plt.xlabel('Año de Incendio')
    plt.ylabel('Promedio de Acres Quemados')
    plt.xticks(rotation=45)
    plt.tight_layout()

   
    plt.show()
else:
    print(f"No hay datos disponibles para el estado: {estado_especifico}.")