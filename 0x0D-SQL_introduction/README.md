### 0-list_databases.sql
- Description: Script to list all databases in the MySQL server.
- Usage: `cat 0-list_databases.sql | mysql -hlocalhost -uroot -p`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 1-create_database_if_missing.sql
- Description: Script to create a database named `hbtn_0c_0` if it doesn't exist.
- Usage: `cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 2-remove_database.sql
- Description: Script to delete the `hbtn_0c_0` database if it exists.
- Usage: `cat 2-remove_database.sql | mysql -hlocalhost -uroot -p`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 3-list_tables.sql
- Description: Script to list all tables in a specified database.
- Usage: `cat 3-list_tables.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 4-first_table.sql
- Description: Script to create a table named `first_table` in the specified database.
- Usage: `cat 4-first_table.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 5-full_table.sql
- Description: Script to print the full description of the `first_table` from the specified database.
- Usage: `cat 5-full_table.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 6-list_values.sql
- Description: Script to list all rows of the `first_table` from the specified database.
- Usage: `cat 6-list_values.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 7-insert_value.sql
- Description: Script to insert a new row into the `first_table` in the specified database.
- Usage: `cat 7-insert_value.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 8-count_89.sql
- Description: Script to display the number of records with id = 89 in the `first_table`.
- Usage: `cat 8-count_89.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 9-full_creation.sql
- Description: Script to create a table named `second_table` and add multiple rows in the specified database.
- Usage: `cat 9-full_creation.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 10-top_score.sql
- Description: Script to list all records of `second_table` ordered by score (descending).
- Usage: `cat 10-top_score.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 11-best_score.sql
- Description: Script to list records with a score >= 10 in `second_table` ordered by score (descending).
- Usage: `cat 11-best_score.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 12-no_cheating.sql
- Description: Script to update the score of Bob to 10 in `second_table` without using Bob’s id value.
- Usage: `cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 13-change_class.sql
- Description: Script to remove all records with a score <= 5 in `second_table`.
- Usage: `cat 13-change_class.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 14-average.sql
- Description: Script to compute the score average of all records in `second_table`.
- Usage: `cat 14-average.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 15-groups.sql
- Description: Script to list the number of records with the same score in `second_table` sorted by the number of records (descending).
- Usage: `cat 15-groups.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 16-no_link.sql
- Description: Script to list all records of `second_table` without rows without a name value, ordered by descending score.
- Usage: `cat 16-no_link.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 101-avg_temperatures.sql
- Description: Script to display the average temperature (Fahrenheit) by city ordered by temperature (descending).
- Usage: `cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS

### 103-max_state.sql
- Description: Script to display the max temperature of each state ordered by State name.
- Usage: `cat 103-max_state.sql | mysql -hlocalhost -uroot -p <database_name>`
- Requirements: MySQL server, Ubuntu 20.04 LTS
