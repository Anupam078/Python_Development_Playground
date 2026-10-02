import httpx

def classify_status(code: int) -> str:
    if code in [200, 201]:
        return "success"
    elif code in [400, 401, 404]:
        return "client_error"
    elif code == 429:
        return "rate_limited"
    elif code >= 500:
        return "server_error"
    else:
        return "unknown"

# Send the GET request
response = httpx.get("https://httpbin.org/get")

# 1. Status Code
print("Status Code:", response.status_code)

# 2. Response Headers
print("\nResponse Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

# 3. JSON Body
print("\nJSON Body:")
data = response.json()
print("URL echoed back:", data.get("url"))
print("Origin IP:", data.get("origin"))

import httpx

# GET: Read data
res_get = httpx.get("https://api.example.com/items")

# POST: Create data (pass a Python dict to `json=`)
res_post = httpx.post("https://api.example.com/items", json={"name": "Widget", "price": 25})

# PUT: Replace data
res_put = httpx.put("https://api.example.com/items/42", json={"name": "Updated Widget", "price": 30})

# PATCH: Partial update
res_patch = httpx.patch("https://api.example.com/items/42", json={"price": 35})

# DELETE: Remove data
res_delete = httpx.delete("https://api.example.com/items/42")

custom_headers = {
    "Authorization": "Bearer my_secret_token_abc123",
    "Accept": "application/json",
    "User-Agent": "MyAgent/1.0",
    "X-Request-ID": "trace_uuid_999"
}

response = httpx.post(
    "https://api.example.com/agent/chat",
    headers=custom_headers,
    json={"prompt": "Hello!"}
)

user_id = 42

# Path param in URL, query params in params dict
response = httpx.get(
    f"https://api.example.com/users/{user_id}/orders",
    params={"status": "shipped", "limit": 10}
)
# Under the hood, httpx constructs:
# https://api.example.com/users/42/orders?status=shipped&limit=10

if response.status_code == 200:
    print("Success:", response.json())
elif response.status_code == 201:
    print("Created successfully!")
elif response.status_code == 429:
    # Rate limited! Check how long to wait
    wait_seconds = response.headers.get("Retry-After", 5)
    print(f"Rate limited. Waiting {wait_seconds}s before retrying...")
elif response.status_code == 422:
    print("Validation error: check your payload fields:", response.json())
elif response.status_code >= 500:
    print("Server error; might be transient.")