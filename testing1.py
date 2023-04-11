import requests

api_key = "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"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

url = "https://api.openai.com/v1/chat/completions"

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Write a brief summary of the advantages and disadvantages of renewable energy.?"}],
    "max_tokens": 50,
    "n": 1,
    "stop": None,
    "temperature": 1.0,
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
