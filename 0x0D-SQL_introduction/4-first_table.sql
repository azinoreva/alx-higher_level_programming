-- creates a table called first_table in the current database in your MySQL server.
-- execute: cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
