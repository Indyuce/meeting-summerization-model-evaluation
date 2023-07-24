#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

MAX_SAMPLES = 10
MAX_SEQUENCE_LENGTH = 6000

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('samples')
mkdir('samples/texts')
mkdir('samples/summaries')

# Login to HF
perform_login()
# https://huggingface.co/datasets/TalTechNLP/AMIsum
dataset = load_dataset("TalTechNLP/AMIsum", split='test')
print(dataset.features)
print('Found total of', len(dataset), 'samples')
indices = list(range(len(dataset)))
random.shuffle(indices)

model_name = 'legendhasit/xgen-7b-8k-inst-8bit'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

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
    tokenized_length = len(tokenizer(dialogue, return_tensors="pt").to('cuda')['input_ids'][0])
    if tokenized_length > MAX_SEQUENCE_LENGTH:
        print('-- Skipped high length sample ' + id + ':', tokenized_length)
        skipped += 1
        continue

    counter += 1

    # Write to file
    target_text_file = open('samples/texts/sample_' + str(counter) + '_' + str(tokenized_length) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()
    
    target_text_file = open('samples/summaries/sample_' + str(counter) + '_' + str(tokenized_length) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print('Found', counter, 'samples after skipping', skipped, 'samples')