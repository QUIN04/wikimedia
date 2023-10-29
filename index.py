import csv
import requests

def read_csv(csvfile='Task 2 - Intern.csv'):
  url_list = []
  with open(csvfile) as file:
    csv_reader = csv.reader(file, delimiter=' ')
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
      url_list.append(row[0])
  return url_list

def get_url_status(url):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate'
  }
  try:
    print(f"Processing URL: {url}")
    response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
    status = response.status_code
  except requests.exceptions.RequestException as e:
    print(f"Request failed for URL: {url}\nError: {e}")
    status = 'failed'
  print(f"URL status: {status}")
  return f"({status}) {url}"

def main():
  statuses = []
  for url in read_csv():
    statuses.append(get_url_status(url))
  print("\nOUTPUT:\n")
  for status in statuses:
    print(status)

if __name__ == "__main__":
  main()
