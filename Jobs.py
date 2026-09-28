import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,or;q=0.5',
    'accept-profile': 'public',
    'apikey': os.getenv('MY_API_KEY'),
    'authorization': os.getenv('MY_BEARER_TOKEN'),
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
    'select': 'id,Company,Location,Salary,Created_At,Category,application_count,posts_link,"Primary Domain","Company Type","Industry Type","Stipend Range","Functional Tags","Technology Tags",is_exclusive',
    'order': 'Created_At.desc.nullslast,id.desc',
    'offset': '0',
    'limit': '100',
}

response = requests.get(
    'https://auth.mystudentclub.com/rest/v1/Industrial%20Training%20Job%20Portal',
    params=params,
    headers=headers,
)
# 1. Get the data
data = response.json()

    # 2. Save it into a new file neatly
with open("all_jobs.json", "w") as file:
        json.dump(data, file, indent=4)
print("Finished! Check your folder for the new file.")
