import requests
from bs4 import BeautifulSoup
import pandas as pd

# Web Scraping
url = "https://realpython.github.io/fake-jobs/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

jobs = []
for job in soup.find_all("div", class_="card-content"):
    jobs.append({
        "Job Title": job.find("h2", class_="title").text.strip(),
        "Company": job.find("h3", class_="company").text.strip(),
        "Location": job.find("p", class_="location").text.strip()
    })

df = pd.DataFrame(jobs)

# READ
print("Original Data:")
print(df.head())

# CREATE
new_job = pd.DataFrame({
    "Job Title": ["AI Intern"],
    "Company": ["OpenAI"],
    "Location": ["Hyderabad"]
})

df = pd.concat([df, new_job], ignore_index=True)

# UPDATE
df.loc[df["Job Title"] == "AI Intern", "Location"] = "Bengaluru"

print("\nAfter Create & Update:")
print(df.tail())

# DELETE
df = df[df["Job Title"] != "AI Intern"]
df.drop("Location", axis=1, inplace=True)

print("\nFinal Data:")
print(df.head())
