import os, shutil
from transformers import AutoTokenizer
import tiktoken

samples = os.listdir('input/texts')
samples = [sample[:-4] for sample in samples if sample.endswith('.txt')]
samples.sort()
samples = samples[:10]
print(samples)

def mkdir(path):
    try:
        os.mkdir(path)
    except:
        pass

# Load xgen tokenizer
model_name = 'Salesforce/xgen-7b-8k-inst'
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

mkdir('halluc.ignored')
for sample in samples:
    #mkdir('halluc/' + sample)
    #shutil.copyfile('input/summaries/' + sample + '.txt', 'halluc.ignored/' + sample + '/gold.txt')
    #shutil.copyfile('input/texts/' + sample + '.txt', 'halluc.ignored/' + sample + '/transcript.txt')
    #shutil.copyfile('intermediate/xgen_7b_2sl_1kt/' + sample + '.txt', 'halluc.ignored/' + sample + '/1kt.txt')
    #shutil.copyfile('intermediate/xgen_7b_2sl_5kt/' + sample + '.txt', 'halluc.ignored/' + sample + '/5kt.txt')

    result_file_1kt = open('intermediate/xgen_7b_2sl_1kt/' + sample + '.txt', 'r', encoding='utf-8')
    length_1kt = len(tokenizer(result_file_1kt.read())['input_ids'])
    result_file_1kt.close()

    result_file_5kt = open('intermediate/xgen_7b_2sl_5kt/' + sample + '.txt', 'r', encoding='utf-8')
    length_5kt = len(tokenizer(result_file_5kt.read())['input_ids'])
    result_file_5kt.close()

    print(length_1kt)
    print(length_5kt)

    length_file = open('halluc.ignored/' + sample + '/zzz_length_' + str(length_1kt) + '_' + str(length_5kt), 'w', encoding='utf-8')
    length_file.write('a')
    length_file.close()