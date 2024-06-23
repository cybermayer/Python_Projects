
import pandas

# Read the CSV file containing the NATO phonetic alphabet into a DataFrame
data = pandas.read_csv(r"nato_phonetic_alphabet.csv")

# Convert the DataFrame into a dictionary
data_dict = data.to_dict()

# Create a new DataFrame from the dictionary (though redundant here, it keeps the data format consistent)
data_frame = pandas.DataFrame(data_dict)

# Initialize an empty string for the word
word = ""

# Create a dictionary from the DataFrame where the key is the letter and the value is the corresponding code
nato_dict = {rows.letter: rows.code for (index, rows) in data_frame.iterrows()}

# Define a function to generate the NATO phonetic alphabet spelling of a given word
def generate_nato():

    word = (input("Give me the word: ")).upper()
    # Iterate over each letter in the word
    for letter in word:
        try:
            # Print the corresponding NATO code for each letter
            print(f"{nato_dict[letter]}\n")
        except KeyError:
            # Handle cases where the character is not in the alphabet
            print(f"Only alphabetic characters acceptable.")
            generate_nato()

generate_nato()
