# python3
import sys
import argparse
import random
import string
import datetime

# create a polynomial hash from a string
# convert to ascii with ord()
def polyHash(string, prime, x):
    myHash = 0

    for i in reversed(range(0, len(string))):
        myHash = (myHash * x + ord(string[i])) % prime

    return myHash

# precomputation of hashes speeds up things
def precomputeHashes(text, length_pattern, prime, x):
    
    length_text = len(text)

    # create list of precomputet hashes
    H = [None] * (len(text) - length_pattern + 1)

    # start with the last possible string of 'length pattern' in the text
    startString = text[length_text-length_pattern:length_text]
#    print('startstring=' + startString)

    # calc the polyhash of startstring. that is the last possible starting position of pattern in text
    H[length_text-length_pattern] = polyHash(startString, prime, x)

    y = 1

    for i in range(1, length_pattern+1):
        y = (y * x) % prime

    # compute hashes of substrings from tail to the head of text
    for i in reversed(range(0, length_text-length_pattern)):
        H[i] = (x*H[i+1] + ord(text[i]) - y*ord(text[i+length_pattern])) % prime

    # print('TEST')
    # for i in range(0, length_text-length_pattern+1):
    #     print('i=' + str(i) + ':  string=' + text[i:i+length_pattern] + '   hash=' + str(polyHash(text[i:i+length_pattern], prime, x)))
    #     print('i=' + str(i) + ': preHash=' + str(H[i]))


    return H

def get_occurrences_rabin_karp(pattern, text):

    # choose a big prime number
    prime = 100000007

    # choose random number 1<->prime-1
    #x = random.randint(1, prime)
    x = 1

    # 
    result = []

    # calc polynomial hash from the pattern string
    patternHash = polyHash(pattern, prime, x)

    # precompute Hashes for substrings of text
    H = precomputeHashes(text, len(pattern), prime, x)

    for i in range(0, len(text) - len(pattern) + 1):

        # if the hashes are equal, there is a strong chance that the substring equals the pattern (or that it could be a collision of hashValues)
        if patternHash == H[i]:
            # check for equality on actual strings            
            if text[i:i+len(pattern)] == pattern:
                result.append(i)


    return result

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-24'

    parser = argparse.ArgumentParser(description='find pattern in text',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--naive', action='store_true',
                       help='use the naive algorithm')
    parser.add_argument('--fast', action='store_true',
                       help='use the Rabin-Karps algorithm')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            max_length_pattern = 1000
            length_pattern = random.randint(1, max_length_pattern)
            
            pattern_list = []

            for i in range(0, length_pattern):
                pattern_list.append(random.choice(string.ascii_letters))

            pattern = ''.join(pattern_list)

            print(pattern)

            # how often should pattern be embedded in text
            amount_embed = random.randint(1, 10)

            length_text_around_pattern = random.randint(max_length_pattern, max_length_pattern*amount_embed)

            text_list = [pattern] * amount_embed

            for i in range(0, length_text_around_pattern):
                text_list.append(random.choice(string.ascii_letters))

            random.shuffle(text_list)

            text = ''.join(text_list)

            print(text)

            current_time1 = datetime.datetime.now()
            result_fast = get_occurrences_rabin_karp(pattern, text)
            current_time2 = datetime.datetime.now()
            result_naive = get_occurrences_naive(pattern, text)
            current_time3 = datetime.datetime.now()

            print('naive result: ' + ' '.join(map(str, result_naive)))
            print('rabin karp result: ' + ' '.join(map(str, result_fast)))

            if result_fast == result_naive:
                print('OK')
            else:
                print('ERROR')
                sys.exit(1)

            print('runtime: naive=' + str(current_time3-current_time2) + '  fast=' + str(current_time2-current_time1))
            print('------')

    # use the naive algorithm
    elif args.naive:
        print_occurrences(get_occurrences_naive(*read_input()))

    elif args.fast:
        print_occurrences(get_occurrences_rabin_karp(*read_input()))

    # this is called when no arguments are used - the same as with --fast
    else:
        print_occurrences(get_occurrences_rabin_karp(*read_input()))

'''
### 4.3 Find pattern in text

#### Problem Introduction
In this problem, your goal is to implement the Rabin–Karp’s algorithm.  

#### Problem Description
**Task:** In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern in the given text.  
**Input Format:** There are two strings in the input: the pattern P and the text T .    
**Constraints:** 1 ≤ |P | ≤ |T | ≤ 5 · 10^5 . The total length of all occurrences of P in T doesn’t exceed 10^8 . The pattern and the text contain only latin letters.  
**Output Format:** Print all the positions of the occurrences of P in T in the ascending order. Use 0-based indexing of positions in the the text T .  
**Time Limits:** C: 1 sec, C++: 1 sec, Java: 5 sec, Python: 5 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3 sec, Ruby: 3 sec, Scala: 3 sec.  
**Memory Limit:** 512Mb.  

#### Sample 1

*Input:*  
aba  
abacaba  

*Output:*  
0 4  
**Explanation:**  
The pattern aba can be found in positions 0 (abacaba) and 4 (abacaba) of the text abacaba.  

#### Sample 2

*Input:*  
Test  
testTesttesT  

*Output:*  
4  
**Explanation:**  
Pattern and text are case-sensitive in this problem. Pattern T est can only be found in position 4 in the text testT esttesT .

#### Sample 3

*Input:*  
aaaaa  
baaaaaaa  

*Output:*  
1 2 3  

**Explanation:**  
Note that the occurrences of the pattern in the text can be overlapping, and that’s ok, you still need to output all of them.  

#### What to Do
Implement the fast version of the Rabin–Karp’s algorithm from the lectures.  
Some hints based on the problems encountered by learners:  
∙ Beware of integer overflow. Use long long type in C++ and long type in Java where appropriate. Take everything (mod p) as soon as possible while computing something (mod p), so that the numbers are always between 0 and p − 1.  
∙ Beware of taking negative numbers (mod p). In many programming languages, (−2)%5 ̸ = 3%5. Thus you can compute the same hash values for two strings, but when you compare them, they appear to be different. To avoid this issue, you can use such construct in the code: x ← ((a%p) + p)%p instead of just x ← a%p.  
∙ Use operator == in Python instead of implementing your own function AreEqual for strings, because built-in operator == will work much faster.  
∙ In C++, method substr of string creates a new string, uses additional memory and time for that, so use it carefully and avoid creating lots of new strings. When you need to compare pattern with a substring of text, do it without calling substr.  
∙ In Java, however, method substring does NOT create a new String. Avoid using new String where it is not needed, just use substring.

#### Implementation in Python

[4-3_hash_substring.py](4-3_hash_substring.py)

'''