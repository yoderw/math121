alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
random.seed()

#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string, 
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s):
    "your code here"

def num_to_let(x):
    "your code here"

def let_to_num(a):
    "your code here"

def shift_char(char, shift):
    "your code here"

def caesar_enc(plain, key):
    "your code here"

def caesar_dec(cipher, key):
    "your code here"

#############################################################
# Breaking the Caesar cipher
#############################################################

def letter_counts(s):
    "your code here"

def normalize(counts):
    "your code here"

# Uncomment the code below once the functions above are complete
# english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
# normalize(english_freqs)

def distance(observed, expected):
    "your code here"

def caesar_break(cipher, frequencies):
    "your code here"



#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    "your code here"

def vigenere_dec(cipher, key):
    "your code here"


#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    "your code here"

def vig_break_for_length(cipher, klen, frequencies):
    "your code here"

def vig_break(c, maxlen, frequencies):
    "your code here"



#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    "your code here"

def sub_enc(s, k):
    "your code here"

def sub_dec(s, k):
    "your code here"


#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    "your code here"

# Uncomment the code below once the functions above are complete
# english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
# normalize(english_trigrams)

def map_log(d):
    "your code here"

# Uncomment the code below once the functions above are complete
# map_log(english_trigrams) 

def trigram_score(s, english_trigrams):
    "your code here"

def sub_break(cipher, english_trigrams):
    "your code here"


