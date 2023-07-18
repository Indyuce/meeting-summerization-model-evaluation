import shutil
import os
import traceback

# Parameters
DATASET_PATH = '../../Datasets/FredSum_std'

# Script
sample_names = os.listdir(DATASET_PATH)

matches = 0

for random_folder_path in sample_names:
    
    for i in range(10):
        existing_sample_file = open('../xgen_find_prompt_zero_shot/input/fredsum/texts/sample_' + str(i + 1) + '.txt', 'r', encoding='utf-8')
        existing_sample_content = existing_sample_file.readlines()
        existing_sample_file.close()

        try:
            summary_file = open(DATASET_PATH + '/' + random_folder_path + '/txt.txt', 'r', encoding='utf-8')
            summary_file_content = summary_file.readlines()
            summary_file.close()

            if summary_file_content == existing_sample_content:
                matches += 1

                for j in [1, 2, 3, 4]:
                    try:
                        summary_file_path = DATASET_PATH + '/' + random_folder_path + '/sum' + str(j) + '.txt'
                        paste_path = '../xgen_find_prompt_zero_shot/input/fredsum/summaries/sample_' + str(1 + i) + '_' + str(j) + '.txt'
                        shutil.copyfile(summary_file_path, paste_path)
                    except:
                        traceback.print_exc()
                    
        except:
            traceback.print_exc()

print(matches)