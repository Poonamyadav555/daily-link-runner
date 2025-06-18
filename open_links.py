import requests
import datetime
import time

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbycP0bU4tsHOCia7Ej9V1kr8lnaf_2hrh_DWN5Jf-rhK90DPffaHXmeGXIhKo-ABdrH3A/exec"

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

def log_to_google_sheet(url, status, message):
    payload = {
        "url": url,
        "status": status,
        "message": message,
        "eventTimestamp": datetime.datetime.now().isoformat()
    }
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=10)
    except Exception as log_err:
        print(f"LOGGING FAILED: {log_err}")

for url in URLS:
    success = False
    for attempt in range(5):  # Retry 5 times
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            print(f"✅ SUCCESS: {url}")
            log_to_google_sheet(url, "success", f"Status Code: {response.status_code}")
            success = True
            break
        except Exception as e:
            print(f"❌ FAILED ({attempt+1}): {url} — {e}")
            time.sleep(3)  # delay between retries

    if not success:
        log_to_google_sheet(url, "failed", f"All retries failed.")
