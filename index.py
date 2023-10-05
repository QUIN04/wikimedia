import pandas as pd
import requests

# Reading data from the csv
df = pd.read_csv('Task 2 - intern.csv')


for url in df['URL']:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"({response.status_code}) {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")