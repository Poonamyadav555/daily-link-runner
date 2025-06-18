import requests
from datetime import datetime

...

for url in URLS:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            print(f"✅ SUCCESS: {url}")
            requests.post(
                "https://script.google.com/macros/s/AKfycbxqkHnzg5iAiryE15Mo8HuU4OHUEhUYtAZGhlIqqJBF/exec",
                json={
                    "url": url,
                    "status": "success",
                    "message": f"HTTP {response.status_code}",
                    "timestamp": datetime.now().isoformat()
                }
            )
            break
        except Exception as e:
            print(f"❌ FAILED attempt {attempt} for {url}: {e}")
            if attempt == MAX_RETRIES:
                requests.post(
                    "https://script.google.com/macros/s/AKfycbxqkHnzg5iAiryE15Mo8HuU4OHUEhUYtAZGhlIqqJBF/exec",
                    json={
                        "url": url,
                        "status": "failed",
                        "message": str(e),
                        "timestamp": datetime.now().isoformat()
                    }
                )
            else:
                time.sleep(SLEEP_BETWEEN_RETRIES)
