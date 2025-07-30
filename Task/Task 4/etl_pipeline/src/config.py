"""
Author: Ajeyomi Adeodyin Samuel
Email: adedoyinsamuel25@gmail.com
Date: 19-03-2025
"""

URL = "https://imdb236.p.rapidapi.com/imdb/top250-movies"


# Insert movie data
movie_query = """
                INSERT INTO movie (movie_id, url, primary_title, original_title, type, description, 
                primary_image, content_rating, is_adult, runtime_minutes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (movie_id) 
                DO UPDATE SET primary_title = EXCLUDED.primary_title;
"""

# Insert date data
date_query = """
                INSERT INTO date (movie_id, start_year, release_date)
                VALUES (%s, %s, %s)
"""

# Insert finance data
finance_query = """
                INSERT INTO finance (movie_id, budget, gross_worldwide)
                VALUES (%s, %s, %s)
"""

# Insert location data
location_query = """
                INSERT INTO location (movie_id, filming_locations, countries_of_origin)
                VALUES (%s, %s, %s)
"""

# Insert production data
production_query = """
                INSERT INTO production (movie_id, production_company_id, production_company_name)
                VALUES (%s, %s, %s)
"""

# Insert user data
user_query = """
                INSERT INTO user_rating (movie_id, average_rating, num_votes)
                VALUES (%s, %s, %s)
"""

# Insert genre data
genre_query = """
                INSERT INTO genre (movie_id, genre, interest)
                VALUES (%s, %s, %s)
"""
