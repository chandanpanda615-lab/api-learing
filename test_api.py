import os
from dotenv import load_dotenv
import requests

load_dotenv()

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,or;q=0.5',
    'apikey': os.getenv('MY_API_KEY'),
    'authorization': os.getenv('MY_BEARER_TOKEN'),
    'content-profile': 'public',
    'content-type': 'application/json',
    'origin': 'https://www.mystudentclub.com',
    'priority': 'u=1, i',
    'referer': 'https://www.mystudentclub.com/',
    'sec-ch-ua': '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36',
    'x-client-info': 'supabase-js-web/2.97.0',
}

params = {
    'uuid': 'eq.54acdc45-b0bd-4c4b-a9bd-578db48f2a2f',
}

json_data = {
    'last_access_date': '2026-09-28T07:05:02.794Z',
}

response = requests.patch('https://auth.mystudentclub.com/rest/v1/profiles', params=params, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"last_access_date":"2026-09-28T07:05:02.794Z"}'
#response = requests.patch('https://auth.mystudentclub.com/rest/v1/profiles', params=params, headers=headers, data=data)
print("Status Code:", response.status_code)
print("Text:", response.text)