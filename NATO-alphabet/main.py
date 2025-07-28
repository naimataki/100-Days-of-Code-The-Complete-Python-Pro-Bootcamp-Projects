import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("NATO-alphabet/nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

nato_phonetic = [nato_alphabet_dict[letter] for letter in word]

print(nato_phonetic)   

