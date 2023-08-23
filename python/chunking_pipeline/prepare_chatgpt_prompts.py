import os

INTERMEDIATE_FOLDER = 'intermediate/xgen_7b_2sl/'
TARGET_FOLDER = 'intermediate/xgen_7b_2sl_chatgpt/'
PREPROMPT = """Here are multiple summaries of the same meeting. The summaries contain different information. Extract the information from all of the following summaries and recap them in a unique, informative and concise paragraph. Avoid using vague, uninformative or indicative phrasing.

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
