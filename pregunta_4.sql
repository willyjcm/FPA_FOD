4 - ¿Cuál fue el total de acres quemados en el año 2005?

CREATE VIEW total_acres_quemados_2005 AS  
SELECT SUM(fire_size) AS total_acres_quemados  
FROM fires  
WHERE fire_year = 2005;
