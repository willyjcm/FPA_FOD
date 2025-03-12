# Si no tienen Nicegui instalen esto "pip install nicegui"
# y para empezar creando una pag usen esto

"""

from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run()

"""

# Aqui estoy haciendo pruebas
import plotly.express as px
import pandas as pd
import numpy  as np
import sqlite3
from nicegui import ui
conexion = sqlite3.connect(r"C:\Users\NIORKYS\Desktop\Programas Estadisticas\BBDD\FPA_FOD_20170508.sqlite")


with ui.header().classes(replace = "row items-center") as header:
    ui.button(on_click = lambda : left_drawer.toggle(), icon = "Menu").props("flat color = blue")
    with ui.tabs() as tabs:
        
        ui.tab("Portada")
        
        ui.tab("Introduccion")
        
        ui.tab("Objetivos")
        
        ui.tab("Objetivo Nº5")

with ui.footer(value = False) as footer:
    
    dark = ui.dark_mode()
    ui.label('Temas:')
    ui.button('Oscuro', on_click = dark.enable)
    ui.button('Claro', on_click = dark.disable)

with ui.left_drawer().classes("bg-blue-100") as left_drawer:
    ui.label("Menu lateral")

with ui.page_sticky(position = "bottom-right", x_offset = 20, y_offset = 20):
    ui.button(on_click = footer.toggle, icon = "contact_support").props("fab")
    
# Este es el panel inicial donde aparecera la Portada
with ui.tab_panels(tabs, value = "Portada").classes("w-full"):
    with ui.tab_panel("Portada"):
        ui.markdown("""
                    
                    <center> <p> Republica Bolivariana de Venezuela </p>
                    <center> <p> Ministerio del Poder Popular para la Educacion </p>
                    <center> <p> Universidad Central de Venezuela </p>
                    <center> <p> Semestre II </p>
                    <center> <p> Computacion II </p>
                    
                    """)
        
# Apartir de aqui vendria lo demas
    with ui.tab_panel("Introduccion"):
        ui.label("Introduccion")
        
    with ui.tab_panel("Objetivos"):
        ui.label("Introduccion")
        
    with ui.tab_panel("Objetivo Nº5"):
        ui.label("Objetivo Nº5")
        df_tabla1 = pd.read_sql_query("SELECT X.STATE AS ESTADOS,X.Nº_INCENDIOS,Y.Nº_UNIDADES FROM(SELECT F.STATE, COUNT(*) AS Nº_INCENDIOS FROM FIRES F GROUP BY F.STATE ORDER BY Nº_INCENDIOS DESC LIMIT 10) AS X JOIN (SELECT U.STATE, COUNT(*) AS Nº_UNIDADES FROM NWCG_UnitIDActive_20170109 U GROUP BY U.STATE ORDER BY Nº_UNIDADES DESC  ) AS Y ON Y.STATE = X.STATE;",conexion)
        
# Aqui todavia falta

ui.run(title = "Incendios forestales en Estados unidos")