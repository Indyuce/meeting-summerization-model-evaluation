import shutil
import os
import random

# Parameters
N_SAMPLES = 10
DATASET_NAME = 'fredsum'
DATASET_PATH = '../../Datasets/FredSum_std'
SUMMARY_TAKEN = 2 # Quel summary prendre pour fredsum ?

# Script
sample_names = os.listdir(DATASET_PATH)
random_indices = list(range(len(sample_names)))
random.shuffle(random_indices)
random_indices = random_indices[:N_SAMPLES]

# DOES NOT CHECK IF THE TRANSCRIPT IS LONGER THAN 8K UNLIKE AMI

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('input')
mkdir('input/' + DATASET_NAME)
mkdir('input/' + DATASET_NAME + '/texts')
mkdir('input/' + DATASET_NAME + '/summaries')

for random_value in random_indices:

    # Find corresponding folder
    random_folder_path = sample_names[random_value]
    print('Chose "' + random_folder_path + '"')

    # Export files
    previous_file_path = DATASET_PATH + '/' + random_folder_path + '/sum' + str(SUMMARY_TAKEN) + '.txt'
    new_file_path = 'input/' + DATASET_NAME + '/summaries/sample_' + str(i + 1) + '.txt'
    shutil.copyfile(previous_file_path, new_file_path)
    
    previous_file_path = DATASET_PATH + '/' + random_folder_path + '/txt.txt'
    new_file_path = 'input/' + DATASET_NAME + '/texts/sample_' + str(i + 1) + '.txt'
    shutil.copyfile(previous_file_path, new_file_path)