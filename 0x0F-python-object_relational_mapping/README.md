The following scripts can be found here in this folder . 
0-select_states.py:
- This script retrieves and lists all states from the database hbtn_0e_0_usa.

1-filter_states.py:
- This script filters and lists all states with names starting with 'N' from the database hbtn_0e_0_usa.

2-my_filter_states.py:
- This script filters and lists states from the database hbtn_0e_0_usa based on user input, ensuring SQL injection safety.

3-my_safe_filter_states.py:
- Similar to 2-my_filter_states.py, this script filters and lists states from the database hbtn_0e_0_usa based on user input, but it's safe from SQL injection attacks.

4-cities_by_state.py:
- This script lists all cities from the database hbtn_0e_4_usa, sorted by their respective states.

5-filter_cities.py:
- This script lists all cities of a specified state from the database hbtn_0e_4_usa.

6-model_state.py:
- This file contains the class definition of the State model and an instance of Base, using SQLAlchemy.

7-model_state_fetch_all.py:
- This script lists all State objects from the database hbtn_0e_6_usa.

8-model_state_fetch_first.py:
- This script prints the first State object from the database hbtn_0e_6_usa.

9-model_state_filter_a.py:
- This script lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.

10-model_state_my_get.py:
- This script prints the ID of the State object with the specified name from the database hbtn_0e_6_usa.

11-model_state_insert.py:
- This script adds a new State object named "Louisiana" to the database hbtn_0e_6_usa.

12-model_state_update_id_2.py:
- This script changes the name of the State object with ID 2 to "New Mexico" in the database hbtn_0e_6_usa.

13-model_state_delete_a.py:
- This script deletes all State objects with names containing the letter 'a' from the database hbtn_0e_6_usa.

model_city.py:
- This file contains the class definition of the City model, which represents cities in a state, using SQLAlchemy.

14-model_city_fetch_by_state.py:
- This script prints all City objects from the database hbtn_0e_14_usa, sorted by state, using the cities relationship defined in model_city.py.

relationship_city.py:
- Similar to model_city.py, this file contains the City model class definition, now with a relationship to the State model, using SQLAlchemy.

relationship_state.py:
- Similar to model_state.py, this file contains the State model class definition, now with a relationship to the City model, using SQLAlchemy.

100-relationship_states_cities.py:
- This script creates a new State object "California" with a City object "San Francisco" and adds them to the database hbtn_0e_100_usa, utilizing the relationship between State and City models.

