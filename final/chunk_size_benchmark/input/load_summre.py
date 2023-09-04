#pip install --upgrade huggingface_hub

import os
import json
from json_builder import to_json

def mkdir(folder_path):
    try:
        os.mkdir(folder_path)
    except:
        pass

mkdir('summre')

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

counter = 0
for file_name in os.listdir('tmp.ignored'):
    if not(file_name.endswith('_minutes.json')):
        continue

    counter += 1
    print('Reading', file_name)
    cropped = '_'.join(file_name.split('_')[:2])

    # Load minutes > summary
    minutes_file = open('tmp.ignored/' + file_name, 'r', encoding='utf-8')
    summary = json.load(minutes_file)['abstractive_summary']
    minutes_file.close()
    
    transcript_file = open('tmp.ignored/' + cropped + '_merged_CM.json', 'r', encoding='utf-8')
    transcript = to_transcript(json.load(transcript_file))
    transcript_file.close()

    json_object = to_json(transcript, summary)

    target_file = open('summre/sample_' + str(counter) + '.txt', 'w', encoding='utf-8')
    target_file.write(json_object)
    target_file.close()
