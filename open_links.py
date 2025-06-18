import requests

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

for url in URLS:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"✅ SUCCESS: {url}")
    except Exception as e:
        print(f"❌ FAILED: {url} — {e}")
