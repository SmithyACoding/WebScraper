import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()) #looks for the value python in each h2
print(len(python_jobs))

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(location_element.text.strip())
    print()

for job_card in python_job_cards:
    links = job_card.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n") 