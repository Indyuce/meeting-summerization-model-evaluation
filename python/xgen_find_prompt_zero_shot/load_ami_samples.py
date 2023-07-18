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
left = list(range(len(sample_names)))

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('summaries')
mkdir('texts')

for i in range(N_SAMPLES):
    
    # Find random index and remove from list
    random_index = random.randint(0, len(left) - 1)
    random_value = left[random_index]
    left.pop(random_index)

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