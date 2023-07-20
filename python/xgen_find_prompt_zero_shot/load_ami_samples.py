#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

N_SAMPLES = 10
DATASET_NAME = 'ami'
MAX_SEQUENCE_LENGTH = 8192
WARNING_THRESHOLD = 2000

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('input')
mkdir('input/' + DATASET_NAME)
mkdir('input/' + DATASET_NAME + '/texts')
mkdir('input/' + DATASET_NAME + '/summaries')

# Login to HF
perform_login()

dataset = load_dataset("knkarthick/AMI")
train_dataset = dataset['test']
left = list(range(len(train_dataset)))

model_name = 'legendhasit/xgen-7b-8k-inst-8bit'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

i = 0
while len(left) > 0 and i < N_SAMPLES:
    
    # Find random index and remove from list
    random_index = random.randint(0, len(left) - 1)
    random_value = left[random_index]
    left.pop(random_index)

    # Get info from dataset
    dataset_sample = train_dataset[random_index]
    reference = dataset_sample['summary']
    dialogue = dataset_sample['dialogue']

    # Check dialogue length
    tokenized_length = len(tokenizer(dialogue, return_tensors="pt").to('cuda')['input_ids'][0])
    if tokenized_length > MAX_SEQUENCE_LENGTH:
        print('Skipped sample with seq length (' + model_name + '):', tokenized_length)
        continue

    i += 1

    # Write to file
    target_text_file = open('input/ami/texts/sample_' + str(i + 1) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()
    
    target_text_file = open('input/ami/summaries/sample_' + str(i + 1) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print('Found', i, 'samples!')