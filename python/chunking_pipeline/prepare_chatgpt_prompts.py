import os

INTERMEDIATE_FOLDER = 'intermediate/xgen_7b_2sl/'
TARGET_FOLDER = 'intermediate/xgen_7b_2sl_chatgpt/'
PREPROMPT = """Here are multiple summaries of the same meeting. Merge all of their information into a unique, concise and informative paragraph.

"""

for sample_name in os.listdir('input/texts'):
    if not(sample_name.endswith('.txt')):
        continue

    sample_file = open(INTERMEDIATE_FOLDER + sample_name, 'r', encoding='utf-8')
    sample = sample_file.read()
    sample_file.close()

    target_file = open(TARGET_FOLDER + sample_name, 'w', encoding='utf-8')

    target_file.write(PREPROMPT)

    target_file.write(sample)
    target_file.close()
