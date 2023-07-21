#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

MAX_SAMPLES = 10
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
    target_text_file = open('input/ami/texts/sample_' + str(counter) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()
    
    target_text_file = open('input/ami/summaries/sample_' + str(counter) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print('Found', counter, 'samples after skipping', skipped, 'samples')