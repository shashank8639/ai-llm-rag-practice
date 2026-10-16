import json

with open("response.json", "r") as f:
    data = json.load(f)

content = data["choices"][0]["message"]["content"]
print(content)