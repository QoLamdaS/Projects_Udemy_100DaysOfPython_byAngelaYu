import pandas

the_data = pandas.read_csv("Day_26-100\\The NATO Alphabet Project\\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in the_data.iterrows()} 
user_input = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)
