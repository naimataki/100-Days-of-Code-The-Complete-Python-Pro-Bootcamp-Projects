from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#print(soup.title)

articles = soup.find_all(name="span" ,class_="titleline")
article_texts = []
article_links = []
for title in articles:
    text = title.find(name="a").getText()
    article_texts.append(text)
    link = title.find(name="a").get("href")
    article_links.append(link)
    #print(headline.getText())

title = soup.find(name="span", class_="titleline")
article_tag = title.find(name="a")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvotes = [upvote.getText() for upvote in soup.find_all(name="span", class_="score")]
int_upvotes = [int(upvote.split()[0]) for upvote in article_upvotes]

index_of_heighest_upvotes = int_upvotes.index(max(int_upvotes))
print(article_texts[index_of_heighest_upvotes])
print(article_links[index_of_heighest_upvotes])



#print(article_texts)
#print(article_links)
#print(article_upvotes)

#print(int_upvotes)




#with open("bs4/website.html") as file:
#    contents = file.read()
#
#soup = BeautifulSoup(contents, "html.parser")
##print(soup.title)
##print(soup.title.name) #element name
##print(soup.title.string) #content of element
##print(soup)
##print(soup.prettify())
##print(soup.a)
#
#all_anchor_tags = soup.find_all(name="a")
##print(all_anchor_tags)
#
#for tag in all_anchor_tags:
#    #print(tag.getText())
#    #print(tag.get("href"))
#    pass
#
#heading = soup.find(name="h1", id="name")
##print(heading)
#
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.getText()) #section's text
#
#company_url = soup.select_one(selector="p a")
#print(company_url)
#
#print(soup.select(".heading"))