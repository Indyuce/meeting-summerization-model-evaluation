import csv, os

def find_file_name(folder_path):

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt') and not('Extractif' in file_name or 'Abstractif' in file_name):
            return file_name

    raise Exception('No summary found')

# Open target file
output_file = open('transcript_length.csv', 'w', encoding='utf-8', newline='')
output_writer = csv.writer(output_file)

# Open list of transcripts
transcript_list_file = open('../../resource/scores_include_abs2.csv', 'r', encoding='utf-8')

counter = 0
for row in csv.reader(transcript_list_file):
    
    counter += 1
    if counter == 1:
        continue

    # Find corresponding file
    folder_path = '../../resource/' + row[0]
    file_name = find_file_name(folder_path)
    file_path = folder_path + '/' + file_name
    transcript_file = open(file_path, 'r', encoding = 'utf-8')

    # Find length
    folder_path = folder_path[len('../../resource/'):]
    file_length = len(transcript_file.read())
    print(folder_path, '>', file_length)
    output_writer.writerow([folder_path, file_length])

    transcript_file.close()

transcript_list_file.close()

output_file.close()