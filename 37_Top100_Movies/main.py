import requests  
from bs4 import BeautifulSoup  

URL = "https://www.empireonline.com/movies/features/best-movies-2/"  

response = requests.get(URL)  # Send a GET request to fetch the webpage
website_html = response.text  # Get the HTML content of the webpage

soup = BeautifulSoup(website_html, "html.parser")  # Create a BeautifulSoup object to parse the HTML

# Find all <h3> elements with class "title", which contain movie titles
all_movies = soup.find_all(name="h3", class_="title")

# Extract text of each movie title and store in a list
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the list of movie titles to match the expected order
movies = movie_titles[::-1]

# Write the movie titles to a text file named "movies.txt"
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")  # Write each movie title followed by a newline
