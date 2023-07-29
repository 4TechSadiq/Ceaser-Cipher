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
