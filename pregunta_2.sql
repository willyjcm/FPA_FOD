-- ¿CUAL ES EL INCENDIO MAS GRANDE REGISTRADO EN TERMINOS DE SUPERFICIE Y EN QUE ESTADO OCURRIO?
CREATE VIEW PREGUNTA_2 AS
SELECT 
    State AS ESTADO,
    ROUND(MAX(FIRE_SIZE) * 0.00404686, 2) AS km2
FROM 
    Fires
GROUP BY 
    State
ORDER BY 
    km2 DESC
LIMIT 1;
