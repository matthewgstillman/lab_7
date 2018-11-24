#Lab 7
#1. Write a program that simulates the magic 8 ball.
# Create a list with at least 10 responses from the list above
# Ask user to ask a question. For example, will I ace my exam today?
# Use the choice() to select one response at random and return it
import random
user_answers = []
eight_ball_answer_list = ['It is Certain','It is decidely so','Without a doubt','Yes definitely','You may rely on it','As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful",]

for i in range(0,10):
  if i == 0:
    user_question = input("Ask a question:")
  if i > 0:
    user_question = input("Ask another question:")
  if '?' in user_question:
    answer = random.choice(eight_ball_answer_list)
    print("{}\n{}".format(user_question, answer))
  else:
    answer = random.choice(eight_ball_answer_list)
    print("{}?\n{}".format(user_question, answer))

#2. Write a program that assigns “codes” to each letter of the alphabet. For example,
#codes = {“a”: “%”, “b”:”9”, “c”:”?”,….}
#Write a function that takes in this dictionary and a sentence to encrypt the sentence.
#Write another function that takes the encrypted sentence and decrypt it

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '," ' ", '?']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '⁄', '€', '‹', '›', '‡', '—', '≠', '±' 'œ', '∑', '®', '†', '¥', '¨', 'ˇ', 'ø', 'å', 'ß', '∂', 'ƒ', '©', '∆']
code_key_dict = dict(zip(letters, symbols))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',"'", '?']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '⁄', '€', '‹', '›', '‡', '—', '≠', '±' 'œ', '∑', '®', '†', '¥', '¨', 'ˇ', 'ø', 'å', 'ß', '∂', 'ƒ', '©', '∆']
code_key_dict = dict(zip(letters, symbols))
print("Code Key Dictionary: {}".format(code_key_dict))

def encrypt(dictionary, sentence):
  lower_case_sentence = sentence.lower()
  encrypted_string = ""
  for i in range(0, len(lower_case_sentence)):
    j = lower_case_sentence[i]
    print("j = {}".format(j))
    encrypted_string += dictionary[j]

  print("Final Enrcypted Sentence: {}".format(encrypted_string))

encrypt(code_key_dict, "Is it going to rain today?")



def decrypt(dictionary, encrypted_sentence):
  decrypted_sentence = ""
  for i in range(0, len(encrypted_sentence)):
    j = encrypted_sentence[i]
    print(list(dictionary.keys())[list(dictionary.values()).index(j)]) 
    decrypted_sentence += list(dictionary.keys())[list(dictionary.values()).index(j)]

  print("Final Decrpyted Sentence: {}".format(decrypted_sentence.capitalize()))


decrypt(code_key_dict, "⁄†ƒ⁄¥ƒ&≠⁄—&ƒ¥≠ƒ®!⁄—ƒ¥≠$!ß∆")

#3. Create a dictionary of phonebooks from the following people
#John ---- 408-999-9000
#Peter --- 408-677-1020
#Jenny ---408-228-1011
#Then write a program that output a LIST containing all the names of the people in the phonebook. 

names = ['John', 'Peter', 'Jenny']
numbers = ['408-999-9000', '408-677-1020', '408-228-1011']

dictionary = dict(zip(names, numbers))
print("Dictionary: {}".format(dictionary))

#Notes

#invert
word_count = {
  "an": 3,
  "a": 4,
  'the': 3,
  'and': 4
}
# inv_map = { v: k for k, v in word_count.items()}
inv_map = {}
for  k, v in word_cound.items():
    inv_map[v] = inv_map.get(v, [])
    inv_map.append(k)
print(inv_map)
    

