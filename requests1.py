import requests

response = requests.get("http://aosabook.org/en/posa/introduction.html")

print(f"status code: " {response.status_code} )
print(f"content length: " {response.headers['content-length']})

print(response.text)