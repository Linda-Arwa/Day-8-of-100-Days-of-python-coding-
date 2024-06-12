# A program that encodes and decodes words for security purposes

# Solution

from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
# Create a function called 'caesar' that takes the 'text' and 'shift' and 'position' as inputs.

def caesar(text, shift, direction):
  if direction == "encode":
    cipher_text = ""
    for char in text:
      if char in alphabet: # This helps us separate non letters like symbols and numbers
        position = alphabet.index(char)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
      else:
        cipher_text += char
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode":
    decrypted_text = ""
    for char in text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position - shift
        new_alphabet = alphabet[new_position]
        decrypted_text += new_alphabet
      else:
        decrypted_text += char
    print(f"The decrypted text is {decrypted_text}")
  else:
    print("Kindly choose either encode or decode")
    
    
# a while loop to allow a user enter other words to decode or encode by asking if they want to run the program again, if they say no the loop ends and tells them goodbye
should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26 # this caters for very big shift vaues eg a shift of 80
  caesar(text, shift, direction)    # function call
  
  result = input("Type 'Yes' if you want to go again. Otherwise, type 'no'\n")
  if result == "no":
    should_continue = False
    print("Goodbye")
    
