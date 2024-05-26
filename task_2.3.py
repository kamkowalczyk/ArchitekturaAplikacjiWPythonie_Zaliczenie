import requests
import threading

countries = [
    "United States", "Canada", "United Kingdom", "Australia", "Germany",
    "France", "Japan", "China", "Brazil", "Russia",
    "India", "Mexico", "South Africa", "Italy", "Spain"
]

def fetch_universities(country, results):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    if response.status_code == 200:
        universities = [uni['name'] for uni in response.json()]
        results[country] = universities

results = {}

threads = []

for country in countries:
    thread = threading.Thread(target=fetch_universities, args=(country, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for country, universities in results.items():
    universities_list = ', '.join(universities)
    print(f"{country}: [{universities_list}]")
