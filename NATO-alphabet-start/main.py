import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

new_dict = {data.letter: data.code for index, data in df.iterrows()}

name = input('Please enter the name: ').upper()

print({each: new_dict[each] for each in name})
