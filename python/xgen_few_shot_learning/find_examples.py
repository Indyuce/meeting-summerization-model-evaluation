#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

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

csv_file = open('sequence_token_length.csv', 'w', encoding = 'utf-8')

for i in range(len(dataset)):
    
    # Sample info
    sample = dataset[i]
    summary = sample['summary']
    transcript = sample['transcript']
    id = sample['id']

    tokenized_length = len(tokenizer(dialogue, return_tensors="pt").to('cuda')['input_ids'][0])

    # Write
    csv_file.write(id + ' -> ' + str(tokenized_length))

csv_file.close()
print('Done!')

"""

print(dataset.features)
print('Found total of', len(dataset), 'samples')
indices = list(range(len(dataset)))
random.shuffle(indices)


def format_transcript(transcript):
    return transcript.replace(' <', '\n<')

counter = 0
skipped = 0
for random_index in indices:
    if counter >= MAX_SAMPLES:
        break

    # Get info from dataset
    dataset_sample = dataset[random_index]
    reference = dataset_sample['summary']
    id = dataset_sample['id']
    dialogue = format_transcript(dataset_sample['transcript'])

    # Check dialogue length
    if tokenized_length > MAX_SEQUENCE_LENGTH:
        print('-- Skipped high length sample ' + id + ':', tokenized_length)
        skipped += 1
        continue

    counter += 1

    # Write to file
    target_text_file = open('input/ami/texts/sample_' + str(counter) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()
    
    target_text_file = open('input/ami/summaries/sample_' + str(counter) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print('Found', counter, 'samples after skipping', skipped, 'samples')
"""

