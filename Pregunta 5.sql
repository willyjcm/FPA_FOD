BEGIN TRANSACTION;
CREATE VIEW TOP_5_CONDADOS_CON_MAYOR_CANTIDAD_DE_INCENDIOS_REGISTRADOS AS
SELECT FIPS_NAME AS NOMBRE_CONDADO, COUNT(*) AS Nº_INCENDIOS
FROM FIRES WHERE NOMBRE_CONDADO IS NOT NULL
GROUP BY NOMBRE_CONDADO
ORDER BY Nº_INCENDIOS DESC 
LIMIT 5;
CREATE VIEW geom_cols_ref_sys AS
SELECT f_table_name, f_geometry_column, geometry_type,
coord_dimension, spatial_ref_sys.srid AS srid,
auth_name, auth_srid, ref_sys_name, proj4text, srtext
FROM geometry_columns, spatial_ref_sys
WHERE geometry_columns.srid = spatial_ref_sys.srid;
CREATE VIEW spatial_ref_sys_all AS
SELECT a.srid AS srid, a.auth_name AS auth_name, a.auth_srid AS auth_srid, a.ref_sys_name AS ref_sys_name,
b.is_geographic AS is_geographic, b.has_flipped_axes AS has_flipped_axes, b.spheroid AS spheroid, b.prime_meridian AS prime_meridian, b.datum AS datum, b.projection AS projection, b.unit AS unit,
b.axis_1_name AS axis_1_name, b.axis_1_orientation AS axis_1_orientation,
b.axis_2_name AS axis_2_name, b.axis_2_orientation AS axis_2_orientation,
a.proj4text AS proj4text, a.srtext AS srtext
FROM spatial_ref_sys AS a
LEFT JOIN spatial_ref_sys_aux AS b ON (a.srid = b.srid);
CREATE VIEW vector_layers AS
SELECT 'SpatialTable' AS layer_type, f_table_name AS table_name, f_geometry_column AS geometry_column, geometry_type AS geometry_type, coord_dimension AS coord_dimension, srid AS srid, spatial_index_enabled AS spatial_index_enabled
FROM geometry_columns
UNION
SELECT 'SpatialView' AS layer_type, a.view_name AS table_name, a.view_geometry AS geometry_column, b.geometry_type AS geometry_type, b.coord_dimension AS coord_dimension, b.srid AS srid, b.spatial_index_enabled AS spatial_index_enabled
FROM views_geometry_columns AS a
LEFT JOIN geometry_columns AS b ON (Upper(a.f_table_name) = Upper(b.f_table_name) AND Upper(a.f_geometry_column) = Upper(b.f_geometry_column))
UNION
SELECT 'VirtualShape' AS layer_type, virt_name AS table_name, virt_geometry AS geometry_column, geometry_type AS geometry_type, coord_dimension AS coord_dimension, srid AS srid, 0 AS spatial_index_enabled
FROM virts_geometry_columns;
CREATE VIEW vector_layers_auth AS
SELECT 'SpatialTable' AS layer_type, f_table_name AS table_name, f_geometry_column AS geometry_column, read_only AS read_only, hidden AS hidden
FROM geometry_columns_auth
UNION
SELECT 'SpatialView' AS layer_type, a.view_name AS table_name, a.view_geometry AS geometry_column, b.read_only AS read_only, a.hidden AS hidden
FROM views_geometry_columns_auth AS a
JOIN views_geometry_columns AS b ON (Upper(a.view_name) = Upper(b.view_name) AND Upper(a.view_geometry) = Upper(b.view_geometry))
UNION
SELECT 'VirtualShape' AS layer_type, virt_name AS table_name, virt_geometry AS geometry_column, 1 AS read_only, hidden AS hidden
FROM virts_geometry_columns_auth;
CREATE VIEW vector_layers_field_infos AS
SELECT 'SpatialTable' AS layer_type, f_table_name AS table_name, f_geometry_column AS geometry_column, ordinal AS ordinal, column_name AS column_name, null_values AS null_values, integer_values AS integer_values, double_values AS double_values, text_values AS text_values, blob_values AS blob_values, max_size AS max_size, integer_min AS integer_min, integer_max AS integer_max, double_min AS double_min, double_max double_max
FROM geometry_columns_field_infos
UNION
SELECT 'SpatialView' AS layer_type, view_name AS table_name, view_geometry AS geometry_column, ordinal AS ordinal, column_name AS column_name, null_values AS null_values, integer_values AS integer_values, double_values AS double_values, text_values AS text_values, blob_values AS blob_values, max_size AS max_size, integer_min AS integer_min, integer_max AS integer_max, double_min AS double_min, double_max double_max
FROM views_geometry_columns_field_infos
UNION
SELECT 'VirtualShape' AS layer_type, virt_name AS table_name, virt_geometry AS geometry_column, ordinal AS ordinal, column_name AS column_name, null_values AS null_values, integer_values AS integer_values, double_values AS double_values, text_values AS text_values, blob_values AS blob_values, max_size AS max_size, integer_min AS integer_min, integer_max AS integer_max, double_min AS double_min, double_max double_max
FROM virts_geometry_columns_field_infos;
CREATE VIEW vector_layers_statistics AS
SELECT 'SpatialTable' AS layer_type, f_table_name AS table_name, f_geometry_column AS geometry_column, last_verified AS last_verified, row_count AS row_count, extent_min_x AS extent_min_x, extent_min_y AS extent_min_y, extent_max_x AS extent_max_x, extent_max_y AS extent_max_y
FROM geometry_columns_statistics
UNION
SELECT 'SpatialView' AS layer_type, view_name AS table_name, view_geometry AS geometry_column, last_verified AS last_verified, row_count AS row_count, extent_min_x AS extent_min_x, extent_min_y AS extent_min_y, extent_max_x AS extent_max_x, extent_max_y AS extent_max_y
FROM views_geometry_columns_statistics
UNION
SELECT 'VirtualShape' AS layer_type, virt_name AS table_name, virt_geometry AS geometry_column, last_verified AS last_verified, row_count AS row_count, extent_min_x AS extent_min_x, extent_min_y AS extent_min_y, extent_max_x AS extent_max_x, extent_max_y AS extent_max_y
FROM virts_geometry_columns_statistics;
COMMIT;
