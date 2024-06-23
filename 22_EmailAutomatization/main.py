# Placeholder for the name to be replaced in the letter format
PLACEHOLDER = "[name]"

# Open the file containing names
with open(r"PATH TO FILE CONTAINING THE NAMES") as names_source:
    names = names_source.readlines()

# Open the file containing the letter format
with open(r"PATH TO FILE CONTAINING THE LETTER FORMATS") as sourcefile:
    text_content = sourcefile.read()
    
    # Remove any leading or trailing whitespace from the name
    for name in names:
        stripped_name = name.strip()
        
        # Replace the placeholder with the current name
        new_letter_content = text_content.replace(PLACEHOLDER, stripped_name)
        
        # Create a new file for each name with the replaced content
        with open(f"PATH TO FOLDER YOU WANT TO STORE THE READY TO SEND LETTERS\letter_for_{stripped_name}.txt", mode="w") as ready_to_send:
            ready_to_send.write(new_letter_content)
