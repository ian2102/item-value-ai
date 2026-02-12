import requests

prompt = f"""
Extract the number of dbs from this message for each item.

Message: [Longbow_8001][Halberd_8001]4dbs/5dbs
[Longbow_8001] Output:
[Halberd_8001] Output:
"""

response = requests.post(
    "http://localhost:8080/completion",
    json={
        "prompt": prompt,
        "n_predict": 128,
        "temperature": 0.0
    }
)

result = response.json()

print(result["content"])
