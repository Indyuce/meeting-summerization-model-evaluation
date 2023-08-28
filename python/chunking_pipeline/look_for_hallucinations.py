import os, shutil

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

mkdir('halluc')

for sample in samples:
    mkdir('halluc/' + sample)
    shutil.copyfile('input/summaries/' + sample + '.txt', 'halluc/' + sample + '/gold.txt')
    shutil.copyfile('input/texts/' + sample + '.txt', 'halluc/' + sample + '/transcript.txt')
    shutil.copyfile('intermediate/xgen_7b_2sl_1kt/' + sample + '.txt', 'halluc/' + sample + '/1kt.txt')
    shutil.copyfile('intermediate/xgen_7b_2sl_1kt/' + sample + '.txt', 'halluc/' + sample + '/5kt.txt')