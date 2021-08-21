import difflib
from difflib import SequenceMatcher

with open('demo1.txt',errors='ignore') as file_1,\
    open('demo2.txt',errors='ignore') as file_2:
    file_1_text = file_1.read()
    file_2_text = file_2.read()
    # a = 'What are you doing'
    # b = "What are you doing?"
    # similarity_check = difflib.SequenceMatcher(None,a,b)
    similarity_check = difflib.SequenceMatcher(None,file_2_text,file_1_text)
    similarity_ratio = similarity_check.ratio() * 100
    print(f'Similarity of : {round(similarity_ratio,4)}%\n')
