import requests

url = 'http://localhost:8000/scrape/'
try:
    response = requests.post(url)

    if response.status_code == 200:
        print('POST request successful')
    else:
        print(f'POST request failed with status code {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'POST request failed: {e}')
