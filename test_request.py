import requests


def execute_code(code: str, timeout: int = 5):
    url = "http://localhost:8000/execute"
    response = requests.post(url, json={"code": code, "timeout": timeout})
    return response.json()


code = """
print("Hello, World!")
result = sum(range(10))
print(f"Sum: {result}")
"""

result = execute_code(code)
print(result)
