from bs4 import BeautifulSoup
import requests
# I put the relevant HTML file on GitHub. In order to fit
# the URL in the book I had to split it across two lines.
# Recall that whitespace-separated strings get concatenated.
url = ("https://raw.githubusercontent.com/"
"joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p') # or just soup.p

first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

first_paragraph_id = soup.p['id'] # raises KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id') # returns None if no 'id'

all_paragraphs = soup.find_all('p') # or just soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
if 'important' in p.get('class', [])]
# Warning: will return the same <span> multiple times
# if it sits inside multiple <div>s.
# Be more clever if that's the case.
spans_inside_divs = [span
for div in soup('div') # for each <div> on the page
for span in div('span')] # find each <span> inside it
from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))
all_urls = list(set(all_urls))
print(len(all_urls))
from typing import Dict, Set
press_releases: Dict[str, Set[str]] = {}
for house_url in all_urls:
   
    soup = BeautifulSoup(house_url, 'html5lib')
    pr_links = {a['href'] for a in soup('a') if 'press releases'
    in a.text.lower()}
    print(f"{house_url}: {pr_links}")
    press_releases[house_url] = pr_links
def paragraph_mentions(text: str, keyword: str) -> bool:
    """
        Returns True if a <p> inside the text mentions {keyword}
    """
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    return any( keyword.lower() in paragraph.lower() for paragraph in paragraphs)