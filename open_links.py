import requests
import time
from datetime import datetime

# === SETTINGS ===
MAX_RETRIES = 50
SLEEP_BETWEEN_RETRIES = 10  # seconds
GOOGLE_APPS_SCRIPT_WEBHOOK = "https://script.google.com/macros/s/AKfycbxqkHnzg5iAiryE15Mo8HuU4OHUEhUYtAZGhlIqqJBF/exec"

# === URL LIST ===
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

# === FUNCTION TO SEND LOG TO SHEET ===
def send_log_to_sheet(url, status, message):
    data = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "url": url,
        "status": status,
        "message": message
    }
    try:
        requests.post(GOOGLE_APPS_SCRIPT_WEBHOOK, json=data, timeout=5)
    except Exception as e:
        print(f"⚠️ Log send failed: {e}")

# === MAIN SCRIPT ===
for url in URLS:
    success = False
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"🔄 Trying {url} (Attempt {attempt})")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            print(f"✅ SUCCESS: {url}")
            send_log_to_sheet(url, "SUCCESS", f"Attempt {attempt}")
            success = True
            break  # Exit retry loop
        except Exception as e:
            print(f"❌ FAILED: {url} — {e}")
            send_log_to_sheet(url, "FAIL", f"Attempt {attempt}: {e}")
            time.sleep(SLEEP_BETWEEN_RETRIES)
    
    if not success:
        print(f"🚫 GAVE UP: {url} after {MAX_RETRIES} attempts")
        send_log_to_sheet(url, "GAVE UP", f"Failed after {MAX_RETRIES} retries")
