#pip install --upgrade huggingface_hub

import shutil
import os
import random
from datasets import load_dataset
from transformers import AutoTokenizer
from huggingface_login import perform_login

MAX_SAMPLES = 12

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('input')
mkdir('input/texts')
mkdir('input/summaries')

# Login to HF
perform_login()
# https://huggingface.co/datasets/TalTechNLP/AMIsum
dataset = load_dataset("TalTechNLP/AMIsum", split='train')
print(dataset.features)
print('Found total of', len(dataset), 'samples')

model_name = 'legendhasit/xgen-7b-8k-inst-8bit'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def format_transcript(transcript):
    return transcript.replace(' <', '\n<')

print('Reading dataset, please wait..')

# Find transcripts and lengths
token_lengths = []
for index in range(len(dataset)):

    # Get info from dataset
    dataset_sample = dataset[index]
    reference = dataset_sample['summary']
    id = dataset_sample['id']
    dialogue = format_transcript(dataset_sample['transcript'])

    # Check dialogue length
    tokenized_length = len(tokenizer(dialogue, return_tensors="pt").to('cuda')['input_ids'][0])
    token_lengths.append((dialogue, tokenized_length, reference))

print('Sorting samples by length..')
#token_lengths = sorted(token_lengths, key=lambda x:x[1], reverse=True)
token_lengths = token_lengths[:MAX_SAMPLES]

print('Outputing to sample folder..')

counter = 0
for pair in token_lengths:
    counter += 1

    dialogue = pair[0]
    tokenized_length = pair[1]
    reference = pair[2]

    # Write to file
    target_text_file = open('input/texts/sample_' + str(counter) + '_' + str(tokenized_length) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()

    target_text_file = open('input/summaries/sample_' + str(counter) + '_' + str(tokenized_length) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print('Found', len(token_lengths), 'samples')