from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all(name="h3" ,class_="title")
movie_texts = []
for title in movies:
    text = title.getText()
    movie_texts.append(text)

print(movie_texts)

movie_texts.reverse()

print(movie_texts)
#
with open("scrape-movie/movies.txt", "w") as file:
    for movie in movie_texts:
        file.write(f"{movie}\n")
