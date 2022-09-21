import random
import os
from random_word import RandomWords

# number of words to draw from for each haystack file
word_bank_size=300

# number of haystack files
n_haystacks=10

# number of words per haystack
haystack_size=100
output_dir='haystack_dir'

r=RandomWords()
os.makedirs(output_dir,exist_ok=True)

include_list=['need','needle','needles','needless']

file_template='haystack{fileno:02d}.txt'


for i in range(n_haystacks):
        print("Generating file %d" %i)
        word_bank=r.get_random_words(limit=word_bank_size-len(include_list))
        if word_bank==None:
            word_bank=r.get_random_words(limit=word_bank_size-len(include_list))

        if len(word_bank) < 10:
            print("I think something went wrong")
            print(i)
        word_bank=word_bank+include_list
        haystack_data=random.choices(word_bank,k=haystack_size)
        with open(output_dir+"/"+file_template.format(fileno=i),"w") as file:
            for word in haystack_data:
                file.write(word+'\n')
