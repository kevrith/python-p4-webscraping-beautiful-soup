from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# Scrape the heading "10 years of shaping tech talent"
selected = doc.select('.heading-financier')
print("Selected elements:", selected)
if selected:
    heading = selected[0].contents[0].strip()
    print(heading)
else:
    print("No elements found with class 'heading-financier'")
    # Since the site has changed, let's scrape the first h1 instead
    h1s = doc.select('h1')
    if h1s:
        print("First h1:", h1s[0].get_text().strip())
    else:
        print("No h1 found")

# Scrape courses from our-courses page
html_courses = requests.get("https://flatironschool.com/our-courses/", headers=headers)
doc_courses = BeautifulSoup(html_courses.text, 'html.parser')

courses = doc_courses.select('.heading-60-black.color-black.mb-20')

for course in courses:
    print(course.contents[0].strip())
