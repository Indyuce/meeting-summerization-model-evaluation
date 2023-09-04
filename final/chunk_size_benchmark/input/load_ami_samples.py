#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
import json
from huggingface_login import perform_login
from json_builder import to_json

MAX_SAMPLES = 30

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('ami')

print('Reading dataset..')

# Login to HF
perform_login()
# https://huggingface.co/datasets/TalTechNLP/AMIsum
dataset = load_dataset("TalTechNLP/AMIsum", split='train')
print('Initial dataset has', len(dataset), 'samples, max', MAX_SAMPLES)
print(dataset.features)

def format_transcript(transcript):
    return transcript.replace(' <', '\n<')

print('Outputing to target folder, please wait..')

# Find transcripts and lengths
token_lengths = []
counter = 0
for index in range(len(dataset)):
    counter += 1
    if counter > MAX_SAMPLES:
        continue

    # Get info from dataset
    dataset_sample = dataset[index]
    dialogue = format_transcript(dataset_sample['transcript'])
    summary = dataset_sample['summary']
    
    # Write to file
    target_text_file = open('ami/sample_' + str(counter) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(to_json(dialogue, summary))
    target_text_file.close()

print('Done!')