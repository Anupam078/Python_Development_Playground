'''Make requests to https://httpbin.org/status/{code} for codes 200, 201, 400, 401, 404, 429, 500
and write a function classify_status(code: int) -> str 
that returns "success", "client_error", "server_error", or "rate_limited" — used correctly across all seven.'''

def classify_Status(code : int) -> str:
    if code == 429:
        return "rate_limited"
    elif code in [400 ,401,404]:
        return 