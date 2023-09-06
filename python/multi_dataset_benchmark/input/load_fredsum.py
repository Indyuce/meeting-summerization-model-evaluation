#pip install --upgrade huggingface_hub

import os
import json
from json_builder import to_json
import random

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('fredsum')

print('Reading dataset..')

def to_transcript(json_object):
    transcript = ""

    for segment in json_object['segments']:
        speaker_id = segment['spk_id'][3:]
        raw = segment['segment']

        turn = '<' + str(speaker_id) + '> ' + raw
        if len(transcript) > 0:
            transcript += "\n"
        transcript += turn
        
    return transcript

root_folder = '../../../Datasets/FredSum_std.ignored/'
folder_names = os.listdir(root_folder)
random.shuffle(folder_names)

counter = 1
for folder_name in folder_names:
    if counter > 30:
        break

    print('Reading', folder_name)

    target_file_path = 'fredsum/sample_' + str(counter) + '.txt'
    counter += 1
    if os.path.isfile(target_file_path):
        print('-- ' + target_file_path + ' already exists, skipping.')
        continue
    
    summaries = []
    for i in range(1, 5):

        try:
            # Load minutes > summary
            summary_file = open(root_folder + folder_name + '/sum' + str(i) + '.txt', 'r', encoding='utf-8')
            summaries.append(summary_file.read())
            summary_file.close()
        except:
            print('-- Could not find summary n' + str(i) + ' of ' + folder_name)
            pass

    transcript_file = open(root_folder + folder_name + '/txt.txt', 'r', encoding='utf-8')
    transcript = transcript_file.read()
    transcript_file.close()

    json_object = to_json(transcript, summaries)

    target_file = open(target_file_path, 'w', encoding='utf-8')
    target_file.write(json_object)
    target_file.close()

print('Done! ')