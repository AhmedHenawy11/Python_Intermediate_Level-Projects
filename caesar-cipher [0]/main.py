from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# STEP 1 Making inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 26:
  shift = shift % 26
#STEP 2 encoding function
def encoding_process( direction, text, shift):
  crypto = ""
  if direction == "encode":
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        crypto += alphabet[position + shift]
      else:
        crypto += letter
    print(f"The encoded text is: {crypto}")
  elif direction == "decode":
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter)
        crypto += alphabet[position - shift]
      else:
        crypto += letter
    print(f"The decoded text is: {crypto}")
encoding_process(direction, text, shift )
#STEP 3 continuis process
choice = input("Type 'yes' if you want to go again, Otherwise type 'no'\n")
while choice == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
  encoding_process(direction, text, shift )
  choice = input("Type 'yes' if you want to go again,    Otherwise type 'no'\n")
print("Goodbye")