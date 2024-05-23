from bs4 import BeautifulSoup
import requests
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies = soup.find_all(name="h3")
movie_titles = [movie.getText() for movie in movies]
reversed_list = movie_titles[::-1]


with open("movies.txt", "w") as data_file:
    for movie in reversed_list:
        data_file.write(f"{movie}\n")

