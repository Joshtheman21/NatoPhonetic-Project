import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

#Using dictionary comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} #iterating through each of data in rows
print(phonetic_dict)

name = input("What's your name? ").upper()
output_list = [phonetic_dict[letter] for letter in name]
#Tapped into our phonetic dictionary and got hold of the value that corresponds with the particular letter
print(output_list)
