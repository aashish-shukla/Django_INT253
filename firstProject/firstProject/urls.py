import requests
import base64

BASE_URL = "http://34.239.60.0:5000/v1"

# Always identify yourself as the "archaeologist"
headers = {
    "User-Agent": "Archaeologist/1.0"
}

# STEP 1: Hit /excavate
resp1 = requests.get(f"{BASE_URL}/excavate", headers=headers)

print("\n--- /excavate response ---")
print("Status:", resp1.status_code)
print("Headers:", resp1.headers)
print("Body:", resp1.json())

# Check all headers for potential auth keys
print("\nAll headers from /excavate:")
for key, value in resp1.headers.items():
    print(f"  {key}: {value}")

# Try different potential auth_key sources
auth_key = None
# Check if there's an auth_key in headers
auth_key = resp1.headers.get("auth_key") or resp1.headers.get("Auth-Key") or resp1.headers.get("authorization")

# If no auth_key in headers, try the etag value
if not auth_key:
    etag_value = resp1.headers.get("etag")
    if etag_value:
        # Remove W/ prefix if present and quotes
        auth_key = etag_value.replace('W/', '').strip('"')

# If still no auth_key, try the code-1 value from response body
if not auth_key:
    response_data = resp1.json()
    auth_key = response_data.get("code-1")

print(f"\nTrying auth_key: {auth_key}")

# Decode the base64 hint from 'data'
data_encoded = resp1.json().get("data")
if data_encoded:
    decoded = base64.b64decode(data_encoded).decode("utf-8")
    print("Decoded message:", decoded)

# STEP 2: Hit /protected with auth_key
if auth_key:
    params = {"auth_key": auth_key}
    resp2 = requests.get(f"{BASE_URL}/protected", headers=headers, params=params)

    print("\n--- /protected response ---")
    print("Status:", resp2.status_code)
    print("Headers:", resp2.headers)
    print("Body:", resp2.text)

    # Extract ETag from headers
    etag = resp2.headers.get("ETag") or resp2.headers.get("etag")
    print(f"\nExtracted ETag (password): {etag}")
    
    # If we get a successful response, try to extract any codes
    if resp2.status_code == 200:
        try:
            response_json = resp2.json()
            print("JSON Response:", response_json)
        except:
            print("Response is not JSON")
else:
    print("No auth_key found to try /protected endpoint")
