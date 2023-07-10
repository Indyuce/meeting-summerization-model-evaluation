import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloomz-1b7"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

file_name = "../resource/sidney_preprompt_unsafe.txt"
with open(file_name, encoding='utf8') as file:
    lines = file.readlines()
input_so_far = '\n'.join(lines)

# Question
prompt = "Who is the president of the republic of France?"
input_so_far += prompt

# Post question
input_so_far += "\n\n* Sydney:"

N = 5
display = True
for i in range(N):
    print(str(i + 1) + '/' + str(N))
    intermediary_output = query({"inputs": input_so_far})

    # No more token length, stop here
    if 'error' in intermediary_output:
        print('Error detected:', intermediary_output['error'])
        display = False
        break
    
    extra_str = intermediary_output[0]['generated_text'][len(input_so_far):]
    old_length = len(input_so_far)
    input_so_far += extra_str
    
    # Stop??
    stop_token = '* Human:'
    try:
        index = extra_str.index(stop_token)
        input_so_far = input_so_far[:old_length + index]
        break
    except:
        pass

if display:
    print(input_so_far)