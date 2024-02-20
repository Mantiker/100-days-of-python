from bs4 import BeautifulSoup
# import lxml

with open("./website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)   # tag + content
# print(soup.title.name)  # tag name
# print(soup.title.string)  # content

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)
