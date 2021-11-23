from jiwer import wer
import math

list_files = ["digit", "digitloop", "digits_ngram"]

for file in list_files:
    with open(f"results/lang_mod/{file}.ref", 'r') as f:
        lines = f.readlines()
        ground = [line.rstrip() for line in lines if line != '\n']
    with open(f"results/lang_mod/{file}.hyp", 'r') as f:
        lines = f.readlines()
        hypothesis = [line.rstrip() for line in lines if line != '\n']
    with open(f"results/lang_mod/{file}.results", 'w') as f:
        error = wer(ground, hypothesis)
        error_percentage = error*100
        confidence = 1.96*math.sqrt(error*(1-error)/len(ground))
        f.write(f'{error}\n')
        f.write(f'Word error rate of {error_percentage}% ± {confidence}%\n')
