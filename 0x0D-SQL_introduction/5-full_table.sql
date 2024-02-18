-- PRINT FULL DESCRIPTON OF THE TABLE first_table

SELECT CONCAT('Table\tCreate Table') AS Description FROM DUAL
UNION ALL
SELECT table_name, create_statement
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
