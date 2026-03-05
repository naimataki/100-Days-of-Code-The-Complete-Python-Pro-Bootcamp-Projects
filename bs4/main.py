from bs4 import BeautifulSoup
import lxml

with open("bs4/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name) #element name
#print(soup.title.string) #content of element
#print(soup)
#print(soup.prettify())
#print(soup.a)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
#print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText()) #section's text

company_url = soup.select_one(selector="p a")
print(company_url)

print(soup.select(".heading"))