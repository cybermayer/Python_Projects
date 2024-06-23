import string

# Define the letters for encryption/decryption, repeating the alphabet multiple times
letters = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
# Split the letters into a list
ltrs = letters.split(", ")

# Ask the user whether they want to encode or decode a message
type = input("Type 'encode' to encryption and 'decode' to decryption: ")
# Ask the user for the message to be processed
message = input("Type the message: ")
# Convert the message to lowercase
lwMessage = message.lower()
# Remove all whitespace from the message
trMessage = lwMessage.translate({ord(c): None for c in string.whitespace})
# Ask the user for the shift value
shift = int(input("Type the shift: "))


def caeser_enc(trMessage) -> None:                            # Function to encrypt the message using Caesar cipher
    
                                                                encrypted = ""  
                                                                nth = 0
                                                                
                                                                for x in range(len(trMessage)):
                                                                    # Find the character's position in the list, shift it, and add to the encrypted message
                                                                    encrypted = encrypted + ltrs[ltrs.index((trMessage[nth])) + shift]
                                                                    nth += 1 
                                                                print(encrypted)  


def caeser_dec(trMessage) -> None:                            # Function to decrypt the message using Caesar cipher
    
                                                                decrypted = ""  
                                                                nth = 0  
                                                                # Loop through each character in the message
                                                                for x in range(len(trMessage)):
                                                                    # Find the character's position in the list, shift it back, and add to the decrypted message
                                                                    decrypted = decrypted + ltrs[ltrs.index((trMessage[nth])) + 26 - shift]
                                                                    nth += 1  
                                                                print(decrypted)  
    

# Execute the appropriate function based on the user's choice
if type == "encode":
    caeser_enc(trMessage)
elif type == "decode":
    caeser_dec(trMessage)
