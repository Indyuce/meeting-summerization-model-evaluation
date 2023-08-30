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

mkdir('halluc.ignored')

for sample in samples:
    mkdir('halluc/' + sample)
    shutil.copyfile('input/summaries/' + sample + '.txt', 'halluc.ignored/' + sample + '/gold.txt')
    shutil.copyfile('input/texts/' + sample + '.txt', 'halluc.ignored/' + sample + '/transcript.txt')
    shutil.copyfile('intermediate/xgen_7b_2sl_1kt/' + sample + '.txt', 'halluc.ignored/' + sample + '/1kt.txt')
    shutil.copyfile('intermediate/xgen_7b_2sl_5kt/' + sample + '.txt', 'halluc.ignored/' + sample + '/5kt.txt')