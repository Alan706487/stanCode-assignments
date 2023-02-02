"""
File: anagram.py
Name: Alan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(s)
            end = time.time()



        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    # _ = []
    # with open(FILE, 'r') as f:
    #     for line in f:
    #         _.append(line.replace('\n', ''))
    # return _
    _ = []
    with open(FILE, 'r') as f:
        for line in f:
            n_line = line.strip()
            # if len(n_line) == len(s):
            if sorted(n_line) == sorted(s):  # 最快 已是答案
                _.append(n_line)
    return _


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    d = read_dictionary(s)
    ans_lst = find_anagrams_helper(s, '', [], d)
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def find_anagrams_helper(s, current_str, ans_lst, d):

    if len(current_str) == len(s):
        # if current_str in read_dictionary(s):  # 會重複加很多次
        if current_str not in ans_lst:
            ans_lst.append(current_str)
            # print(ans_lst)
            print(f'Fond:   {current_str}')
            print('Searching...')
        else:
            pass
    else:
        for ch in s:  # stop
            if ch in current_str and current_str.count(ch) == s.count(ch):
                pass
            else:
                current_str += ch
                if has_prefix(current_str, d):
                    find_anagrams_helper(s, current_str, ans_lst, d)
                current_str = current_str[:-1]
    return ans_lst


def has_prefix(sub_s, d):

    for word in d:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
