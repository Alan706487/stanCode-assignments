"""
File: boggle.py
Name: Alan
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
 """
 TODO:
 """
 activate = True
 start = time.time()
 ####################
 alphabet_lst = []  # 用來裝入字母
 s = ''
 for i in range(4):
  _ = []
  print(i+1, end=' ')
  user_input_s = input('row of letters: ').lower()
  for j in range(len(user_input_s)):
   ch = user_input_s[j]
   _.append(ch)
   if ch != ' ':
    alphabet_lst.append(ch)
    s += ch
  if len(_) == 7 and _[1] and _[3] and _[5] is ' ':
   pass
  else:
   print('Illegal input')
   activate = False
   break
 print(alphabet_lst)
 # if activate is True:
 #  find_anagrams(s)
 ####################
 end = time.time()
 print('----------------------------------')
 print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
 # lst = {}
 lst = set()
 with open(FILE, 'r') as f:
  for line in f:
   lst.add(line.strip())
 return lst


def find_anagrams(s, alphabet_lst):
 dictionary_list = read_dictionary()
 ans_lst = []
 find_anagrams_helper(s, '', ans_lst, alphabet_lst, dictionary_list)


def find_anagrams_helper(s, current_s, ans_lst, alphabet_lst, dictionary_list):
 """
 :param s: string, user entered words.
 :param current_s: string, used for concatenate prefix.
 :param ans_lst: string, record the anagram that match the answer.
 :param dictionary_list: list[str], list of words stored in the dictionary for optimizing recursion.
 -----------------------------------------------------------------------------
 The main purpose is to perform anagram word reorganization.

 Basic Framework
  1. Recursive Case
   1-1. choose     : Insert a letter at the end
   1-2. explore    : recursion.
   1-3. un-choose  : Remove a letter from the end.
  2. Base Case
   2-1. When the word "s" is given to all "current_s".
   2-2. and current_s is not in the answer before it is printed (to avoid duplicate answers).
 Optimization
  Ⅰ. If the first word is in the dictionary, then explore will continue.
 """
 if len(s) == 0:                                 # 2. Base Case
  if current_s in dictionary_list:
   if current_s not in ans_lst:                    # 2-2
    ans_lst.append(current_s)
    print('Found:', current_s)

 else:                                           # 1. Recursive Case
  for i in range(len(s)):
   if is_neighbor(current_s, unused_s, alphabet_lst):
    # 1-1. Choose
    current_s += s[i]
    unused_s = s[0:i]+s[i+1:]
    current_index = len(alphabet_lst) - len(unused_s) - 1
    unused_index =
    # 1-2. Explore
    if has_prefix(current_s, dictionary_list):          # Ⅰ. The first word is in the dictionary.
     if current_s in dictionary_list and len(current_s) >= 4:
      if current_s not in ans_lst:
       ans_lst.append(current_s)
       print('Found:', current_s)
     find_anagrams_helper(unused_s, current_s, ans_lst, alphabet_lst, dictionary_list)

    # 1-3. Un-choose
    current_s = current_s[:-1]


def has_prefix(sub_s, dictionary_list):
 """
 :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
 :return: (bool) If there is any words with prefix stored in sub_s
 """
 for word in dictionary_list:
  if word.startswith(sub_s):
   return True
 return False


def is_neighbor(current_index, unused_index):
 # 角
 if current_index == 0:
  if unused_index == 1 or unused_index == 4 or unused_index == 5:
   return True
 elif current_index == 3:
  if unused_index == 2 or unused_index == 6 or unused_index == 7:
   return True
 elif current_index == 12:
  if unused_index == 8 or unused_index == 9 or unused_index == 13:
   return True
 elif current_index == 15:
  if unused_index == 10 or unused_index == 11 or unused_index == 14:
   return True
 # 邊
 elif current_index == 1 or current_index == 2:
  if unused_index == (current_index-1) or unused_index == (current_index+1) or unused_index == (current_index+3) or unused_index == (current_index+4) or unused_index == (current_index+5):
   return True

 elif current_index == 4 or current_index == 8:
  if unused_index == (current_index-4) or unused_index == (current_index-3) or unused_index == (current_index+1) or unused_index == (current_index+4) or unused_index == (current_index+5):
   return True
 elif current_index == 7 or current_index == 11:
  if unused_index == (current_index - 5) or unused_index == (current_index - 4) or unused_index == (
    current_index - 1) or unused_index == (current_index + 3) or unused_index == (current_index + 4):
   return True

 elif current_index == 13 or current_index == 14:
  if unused_index == (current_index - 5) or unused_index == (current_index - 4) or unused_index == (
    current_index - 3) or unused_index == (current_index - 1) or unused_index == (current_index + 1):
   return True
 # 中間
 elif current_index == 5 or current_index == 6 or current_index == 9 or current_index == 10:
  if unused_index == (current_index-5) or unused_index == (current_index-4) or unused_index == (current_index-3) or unused_index == (current_index-1) or unused_index == (current_index+1) or unused_index == (current_index+3) or unused_index == (current_index+4) or unused_index == (current_index+5):
   return True





if __name__ == '__main__':
 main()