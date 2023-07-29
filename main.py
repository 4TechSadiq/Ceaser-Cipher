alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction,text,shift):
  caesor_out = ""
  if direction == "encode":
    for letter in text:
      text_pos = alphabet.index(letter)
      new_pos = text_pos + shift
      caesor_out+=alphabet[new_pos]
    print(f"your encoded message is {caesor_out}")
  elif direction == "decode":
    for txt in text:
      pos = alphabet.index(txt)
      new_pos = pos - shift
      caesor_out+= alphabet[new_pos]
    print(f"decode msg is {caesor_out}")

caesar(direction,text,shift)
