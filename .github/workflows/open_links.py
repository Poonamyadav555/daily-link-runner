import time
import requests
from datetime import datetime

urls = [
    "https://feebank.in/order/status",
    "https://api.techmutant.com/SchoolUpdates/DailyBirthdays?schoolId=563",
    "https://api.techmutant.com/SchoolUpdates/TeacherBirthdays?schoolId=568",
    "https://AKfycbxqkHnzg5iAiryE15Mo8HuU4OHUEhUYtAZGhlIqqJBF"  # Add more if needed
]

def try_until_success(url):
    attempt = 0
    while True:
        try:
            attempt += 1
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                print(f"{datetime.now()} - ✅ SUCCESS: {url} (Attempt {attempt})")
                return
            else:
                print(f"{datetime.now()} - ❌ FAIL ({response.status_code}): {url} (Attempt {attempt})")
        except Exception as e:
            print(f"{datetime.now()} - ❌ EXCEPTION: {url} (Attempt {attempt}) - {e}")
        time.sleep(10)  # wait before retrying

for url in urls:
    try_until_success(url)
