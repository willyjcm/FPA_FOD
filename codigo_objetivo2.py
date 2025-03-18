
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# 1 Conectar a la base de datos SQLite
conn = sqlite3.connect("FPA_FOD_20170508.sqlite")

# 2 Filtrar los incendios entre 2005 y 2015
query = """
SELECT STATE, STAT_CAUSE_DESCR, COUNT(*) as total_incendios
FROM Fires
WHERE FIRE_YEAR BETWEEN 2005 AND 2015
GROUP BY STATE, STAT_CAUSE_DESCR;
"""
df = pd.read_sql(query, conn)

# 3 traducir las causas al español
traduccion_causas = {
    "Lightning": "Rayo",
    "Equipment Use": "Uso de Equipos",
    "Smoking": "Fumar",
    "Campfire": "Fuego de Campamento",
    "Debris Burning": "Quema de Escombros",
    "Railroad": "Ferrocarril",
    "Arson": "Incendio Provocado",
    "Children": "Niños",
    "Miscellaneous": "Misceláneo",
    "Fireworks": "Fuegos Artificiales",
    "Powerline": "Línea Eléctrica",
    "Structure": "Estructura",
    "Missing/Undefined": "Desconocido"
}

# Aplicar traducción de causas
df["STAT_CAUSE_DESCR"] = df["STAT_CAUSE_DESCR"].map(traduccion_causas)

# 4 10 estados con más incendios
top_estados = df.groupby("STATE")["total_incendios"].sum().nlargest(10).index
df_top = df[df["STATE"].isin(top_estados)]

# 5. lista de todas las causas de incendios 
causas = df_top["STAT_CAUSE_DESCR"].unique()

# 6. Crear un PDF con gráficos y tablas en la misma pág
with PdfPages("incendios_impacto.pdf") as pdf:

    for causa in causas:
        df_causa = df_top[df_top["STAT_CAUSE_DESCR"] == causa]  # Filtrar solo esa causa

        # Crear figura grande 
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))

        #  Gráfico de barras (color azul)
        sns.barplot(data=df_causa, x="STATE", y="total_incendios", color="#1f77b4", ax=axes[0])
        axes[0].set_xlabel("Estado")
        axes[0].set_ylabel("Cantidad de Incendios")
        axes[0].set_title(f"Impacto de '{causa}' en los 10 estados con más incendios (2005-2015)")
        axes[0].tick_params(axis='x', rotation=45)

        #  Tabla con los datos
        axes[1].axis("tight")
        axes[1].axis("off")
        table_data = df_causa[["STATE", "total_incendios"]].values
        column_labels = ["Estado", "Total de Incendios"]
        table = axes[1].table(cellText=table_data, colLabels=column_labels, loc="center", cellLoc="center", colWidths=[0.2, 0.2])

        # Guardar en el PDF
        pdf.savefig(fig)
        plt.close(fig)

# 7. Cerrar conexión
conn.close()

print("El archivo PDF 'incendios_impacto.pdf' ha sido generado correctamente.")
