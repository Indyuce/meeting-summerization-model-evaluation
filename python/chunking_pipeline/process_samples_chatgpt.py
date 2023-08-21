
import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
}

json_data = {
    'input': 'Hey, who are you?',
    'model': 'text-embedding-ada-002',
}

response = requests.post('https://api.openai.com/v1/embeddings', headers=headers, json=json_data)
print(response)
