import csv
import requests

def get_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException:
        return "Error"
        
filename = "Task 2 - intern.csv"  
with open(filename, "r") as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

for url in urls:
    status_code = get_status_code(url)
    print(f"({status_code}) {url}")
