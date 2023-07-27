#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

MAXIMUM_LENGTH = 4096

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

perform_login()
# https://huggingface.co/datasets/TalTechNLP/AMIsum
dataset = load_dataset("TalTechNLP/AMIsum", split='train')

# Load model tokenizer
model_name = 'legendhasit/xgen-7b-8k-inst-8bit'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def format_transcript(transcript):
    return transcript.replace(' <', '\n<')

# Find entries and sort
entries = []
for i in range(len(dataset)):
    
    # Sample info
    sample = dataset[i]
    summary = sample['summary']
    transcript = format_transcript(sample['transcript'])
    id = sample['id']

    tokenized_length = len(tokenizer(transcript, return_tensors="pt").to('cuda')['input_ids'][0])
    if tokenized_length <= MAXIMUM_LENGTH:
        entries.append((id, tokenized_length, summary, transcript))
entries = sorted(entries, key=(lambda entry: entry[1]))

# Write entries to folder
print('Writing to file..')
mkdir('examples')
for entry in entries:
    target_file = open('examples/' + str(entry[1]) + '_' + entry[0] + '.txt', 'w', encoding = 'utf-8')
    target_file.write(entry[3])
    target_file.write('\n----------------------------------------------------------------------------------------\n')
    target_file.write(entry[2])
    target_file.close()

print('Done!')
