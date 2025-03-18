#importación de librerías

import pandas as pd
import plotly.express as px
import numpy as np
import sqlite3


#Conexción con la base de datos limpia (los top 10 de estados con mayores reportes de incendio del 2005 al 2015)

con = sqlite3.connect(r"c:\Datos\Clase de computación\Base de datos Compu II\FPA_FOD_20170508.sqlite\BBDD limpiaTrabajo final\FPA_FOD_20170508.sqlite")


#Selección de los estados: Top 10 de estados con mayores reportes de incendios TX, CA, GA, NY, NC, FL, MS, AZ, AL, SC

#Rango de los días que tardaron en contenerse los incendios y los mismos que fueron contenidor el mismo día en el estado de Texas.

#Texas

df_tiempo_de_contencion_de_los_incendios_en_TX = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'TX'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                           """, con)

#California


df_tiempo_de_contencion_de_los_incendios_en_CA = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'CA'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)


#Georgia

df_tiempo_de_contencion_de_los_incendios_en_GA = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'GA'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                         """, con)


#Nueva York

df_tiempo_de_contencion_de_los_incendios_en_NY = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'NY'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                                                    """, con)

#Carolina del Norte

df_tiempo_de_contencion_de_los_incendios_en_NC = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'NC'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)


#Florida

df_tiempo_de_contencion_de_los_incendios_en_FL = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'FL'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)

#Mississippi

df_tiempo_de_contencion_de_los_incendios_en_MS = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'MS'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)


#Arizona

df_tiempo_de_contencion_de_los_incendios_en_AZ = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'AZ'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)

#Alabama

df_tiempo_de_contencion_de_los_incendios_en_AL = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'AL'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)

#Carolina del Sur

df_tiempo_de_contencion_de_los_incendios_en_SC = pd.read_sql_query("""SELECT
    LOCAL_FIRE_REPORT_ID AS "Reportes de Incendios",
    FIRE_YEAR AS "Año",
    STATE AS Estado,
    DISCOVERY_DOY AS "Día del descubrimiento del incendio",
    CONT_DOY AS "Día de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE ABS(DISCOVERY_DOY - CONT_DOY)
    END AS "Tardanza (en Días) de la contención del incendio",
    CASE
        WHEN ABS(DISCOVERY_DOY - CONT_DOY) = 0 THEN 1
        ELSE 0
    END AS "Incendios contenidos el mismo día"
FROM Fires
WHERE
    STATE = 'SC'
    AND CONT_DOY IS NOT NULL
    AND LOCAL_FIRE_REPORT_ID IS NOT NULL
                                              """, con)





#Cierre de la conexción
con.close()

