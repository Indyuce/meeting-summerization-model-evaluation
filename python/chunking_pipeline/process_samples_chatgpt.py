
import requests

key_file = open('openai_key.ignored', 'r', encoding='utf-8')
key = key_file.read()
key_file.close()

print('Using key', key)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key,
}

json_data = {
    'input': 'Hey, who are you?',
    'model': 'text-embedding-ada-002',
}

response = requests.post('https://api.openai.com/v1/embeddings', headers=headers, json=json_data)
print(response)
