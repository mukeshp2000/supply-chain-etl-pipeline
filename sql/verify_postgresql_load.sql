-- Verify that the ETL pipeline loaded all PostgreSQL tables

SELECT 'customers' AS table_name, COUNT(*) AS row_count
FROM customers

UNION ALL

SELECT 'shipments', COUNT(*)
FROM shipments

UNION ALL

SELECT 'performance', COUNT(*)
FROM performance;