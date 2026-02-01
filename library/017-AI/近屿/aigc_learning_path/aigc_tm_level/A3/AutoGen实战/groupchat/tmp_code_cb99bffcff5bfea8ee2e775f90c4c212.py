import requests
from bs4 import BeautifulSoup
import re

# Step 1: Get the data from arXiv
url = "https://arxiv.org/search/?query=gpt-4&searchtype=all&abstracts=show&order=-announced_date_first&size=50"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find the papers about gpt-4
papers = soup.find_all('p', class_='title is-5 mathjax')
links = soup.find_all('p', class_='list-title is-inline-block')

# Step 3: Analyze the papers and find the potential application in software field
for i in range(len(papers)):
    title = papers[i].text.strip()
    link = links[i].a['href']
    print(f"Title: {title}\nLink: {link}\n")

    # Get the abstract of the paper
    paper_response = requests.get(link)
    paper_soup = BeautifulSoup(paper_response.text, 'html.parser')
    abstract = paper_soup.find('blockquote', class_='abstract mathjax').text.strip()
    print(f"Abstract: {abstract}\n")

    # Check if the abstract mentions about software
    if re.search('software', abstract, re.IGNORECASE):
        print("This paper potentially has applications in the software field.\n")
    else:
        print("This paper does not seem to have applications in the software field.\n")