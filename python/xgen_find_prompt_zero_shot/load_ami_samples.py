import shutil
import os
import random
from datasets import load_dataset

N_SAMPLES = 10
DATASET_NAME = 'ami'

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('input')
mkdir('input/' + DATASET_NAME)
mkdir('input/' + DATASET_NAME + '/texts')
mkdir('input/' + DATASET_NAME + '/summaries')

dataset = load_dataset("TanveerAman/AMI-Corpus-Text-Summarization")
train_dataset = dataset['train']
left = list(range(len(train_dataset)))

for i in range(N_SAMPLES):
    
    # Find random index and remove from list
    random_index = random.randint(0, len(left) - 1)
    random_value = left[random_index]
    left.pop(random_index)

    # Get info from dataset
    dataset_sample = train_dataset[random_index]
    reference = dataset_sample['Summaries']
    dialogue = dataset_sample['Dialogue']

    # Write to file
    target_text_file = open('input/ami/texts/sample_' + str(i + 1) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(dialogue)
    target_text_file.close()
    
    target_text_file = open('input/ami/summaries/sample_' + str(i + 1) + '.txt', 'w', encoding = 'utf-8')
    target_text_file.write(reference)
    target_text_file.close()

print(len(dataset['train']))