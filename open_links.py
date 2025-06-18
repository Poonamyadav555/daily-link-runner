import requests
import time
from datetime import datetime

# Your Apps Script Web App URL
SCRIPT_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbycP0bU4tsHOCia7Ej9V1kr8lnaf_2hrh_DWN5Jf-rhK90DPffaHXmeGXIhKo-ABdrH3A/exec"

URLS = [
    "https://feebank.in/order/status",
    "https://feebank.in/order/otherccavenuestatus/545",
    "https://feebank.in/order/otherccavenuestatus/567",
    "https://feebank.in/order/RazorPayFeeStatus?schoolid=575",
    "https://feebank.in/order/otherccavenuestatus/569",
    "https://feebank.in/order/OtherCcAvenueStatus?id=578",
    "https://feebank.in/order/OtherCcAvenueStatus?id=534",
    "https://feebank.in/order/OtherCcAvenueStatus/605",
    "https://feebank.in/order/OtherCcAvenueStatus/582",
    "https://feebank.in/order/OtherCcAvenueStatus/598",
]

# Timestamp for grouping this run
RUN_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def send_log(url, status, message):
    try:
        requests.get(SCRIPT_WEB_APP_URL, params={
            'url': url,
            'status': status,
            'message': message,
            'run': RUN_TIME
        }, timeout=10)
    except Exception as e:
        print(f"⚠️ Failed to log to sheet: {e}")

def try_until_success(url):
    while True:
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            print(f"✅ SUCCESS: {url}")
            send_log(url, "success", f"Status Code: {response.status_code}")
            break  # Exit loop if success
        except Exception as e:
            print(f"❌ FAILED: {url} — {e}. Retrying in 10s...")
            send_log(url, "failed", str(e))
            time.sleep(10)  # Wait before retrying

# Run each URL until success
for url in URLS:
    try_until_success(url)
