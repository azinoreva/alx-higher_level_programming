
### 0-privileges.sql
- **Purpose:** Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the local server.
- **Instructions:** Execute the script to view privileges for specified users.
- **Additional Notes:** Creates `user_0d_1` if it doesn't exist and grants all privileges.

### 1-create_user.sql
- **Purpose:** Creates the MySQL server user `user_0d_1`.
- **Instructions:** Execute the script to create the user with full privileges.
- **Additional Notes:** Password for `user_0d_1` is set to `user_0d_1_pwd`.

### 2-create_read_user.sql
- **Purpose:** Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege on the database.
- **Instructions:** Execute the script to create the database and user.
- **Additional Notes:** Password for `user_0d_2` is set to `user_0d_2_pwd`.

### 3-force_name.sql
- **Purpose:** Creates the table `force_name` with constraints on the `name` column.
- **Instructions:** Execute the script to create the table `force_name`.
- **Additional Notes:** Ensures the `name` column cannot be null.

### 4-never_empty.sql
- **Purpose:** Creates the table `id_not_null` with a default value for the `id` column.
- **Instructions:** Execute the script to create the table `id_not_null`.
- **Additional Notes:** Ensures the `id` column is never empty.

### 5-unique_id.sql
- **Purpose:** Creates the table `unique_id` with a unique constraint on the `id` column.
- **Instructions:** Execute the script to create the table `unique_id`.
- **Additional Notes:** Ensures the `id` column values are unique.

### 6-states.sql
- **Purpose:** Creates the database `hbtn_0d_usa` and the table `states` within it.
- **Instructions:** Execute the script to create the database and table.
- **Additional Notes:** Defines `id` as primary key and `name` as not null.

### 7-cities.sql
- **Purpose:** Creates the table `cities` within the database `hbtn_0d_usa`.
- **Instructions:** Execute the script to create the table.
- **Additional Notes:** Defines `id` as primary key and `state_id` as a foreign key.

### 8-cities_of_california_subquery.sql
- **Purpose:** Lists all the cities of California without using the JOIN keyword.
- **Instructions:** Execute the script to retrieve the cities.
- **Additional Notes:** Results are sorted by `cities.id`.

### 9-cities_by_state_join.sql
- **Purpose:** Lists all cities contained in the database `hbtn_0d_usa` along with their corresponding states.
- **Instructions:** Execute the script to retrieve the data.
- **Additional Notes:** Results are sorted by `cities.id`.

### 10-genre_id_by_show.sql
- **Purpose:** Lists all shows contained in `hbtn_0d_tvshows` with at least one genre linked.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted by `tv_shows.title` and `tv_show_genres.genre_id`.

### 11-genre_id_all_shows.sql
- **Purpose:** Lists all shows contained in `hbtn_0d_tvshows` along with their genre IDs.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted by `tv_shows.title` and `tv_show_genres.genre_id`.

### 12-no_genre.sql
- **Purpose:** Lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted by `tv_shows.title`.

### 13-count_shows_by_genre.sql
- **Purpose:** Lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted in descending order by the number of shows linked.

### 14-my_genres.sql
- **Purpose:** Lists all genres of the show Dexter from the database `hbtn_0d_tvshows`.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted in ascending order by genre name.

### 15-comedy_only.sql
- **Purpose:** Lists all Comedy shows in the database `hbtn_0d_tvshows`.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted in ascending order by show title.

### 16-shows_by_genre.sql
- **Purpose:** Lists all shows and their linked genres from `hbtn_0d_tvshows`.
- **Instructions:** Execute the script to view the results.
- **Additional Notes:** Results are sorted in ascending order by show title and genre name.
