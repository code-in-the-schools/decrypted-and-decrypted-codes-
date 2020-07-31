# nltk.download()
from nltk.corpus import words

# goal: function that prints all keys and function that prints right key

def open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word)
		output.append(line_words)
	return (output)

#encrypt code

def encrypt_character(character, shift): 
  cipher = ord(character) + shift
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if character in alphabet:
    if cipher > ord("z"):
        cipher -= 26
  else:
      if cipher > ord("Z"):
        cipher -= 26
  return(chr(cipher))

def encrypt_word(word, shift): 
  new_word = ""
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for character in word:
    if character in alphabet:
        new_word += encrypt_character(character, shift)
    else:
        new_word += character
  return(new_word)
  
def encrypt_message(message, shift):
  new_message = []
  for line in message:
    new_line = []
    for word in line:
        new_line.append(encrypt_word(word, shift))
    new_message.append(new_line)
  return new_message
  
#decrypt code

def decrypt_character(character, shift): 
  cipher = ord(character) - shift
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if character in alphabet:
    if cipher < ord("a"):
        cipher += 26
  else:
      if cipher < ord("A"):
        cipher += 26
  return(chr(cipher))

def decrypt_word(word, shift): 
  new_word = ""
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for character in word:
    if character in alphabet:
        new_word += decrypt_character(character, shift)
    else:
        new_word += character
  return(new_word)
  
def decrypt_message(message, shift):
  new_message = []
  for line in message:
    new_line = []
    for word in line:
        new_line.append(decrypt_word(word, shift))
    new_message.append(new_line)
  return new_message


# cracking caesar shift

# print all keys
def print_all(encoded_message):
    for shift in range(1, 26):
        print(decrypt_message(encoded_message, shift), "key: ", shift)

def crack_cipher(encoded_message):
    best_key = 0
    best_counter = 0
    word_list = words.words()
    for shift in range(1, 26):
        counter = 0
        for line in decrypt_message(encoded_message, shift):
            for word in line:
                if word in word_list:
                    counter += 1
        if counter > best_counter:
            best_counter = counter
            best_key = shift
    print(decrypt_message(encoded_message, best_key))
    return best_key


# open file 
encoded_message = open_file("sample.txt")
# encode message
# encoded_message = encrypt_message(plain_text, random.randint(1, 26))
print(crack_cipher(encoded_message))
