# Uses python3
import argparse
import sys
import datetime

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        # print('i am a ' + self.bracket_type)
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def check_brackets_in_code(text):

    opening_brackets_stack = []

    for i, character in enumerate(text):

        # if current character is an opening bracket
        if character == '(' or character == '[' or character == '{':

            # put the opening-bracket-character on the stack
            open_bracket = Bracket(character, i+1)
            opening_brackets_stack.append(open_bracket)

        # if the current character is a closing bracket
        if character == ')' or character == ']' or character == '}':

            if len(opening_brackets_stack) == 0:
                return i+1

            # if last opening bracket matches the closing bracket, remove the opening bracket from stack
            if opening_brackets_stack[-1].match(character):
                # print('closing bracket fits last opening bracket')
                # print('last opening bracket was ' + opening_brackets_stack[-1].bracket_type)
                opening_brackets_stack.pop()

            # if the last opening bracket does not match the closing bracket, return current position
            else:
                # print('closing bracket does not fit last opening bracket')
                # print('last opening bracket was ' + opening_brackets_stack[-1].bracket_type)
                return i+1

    # if whole text has been processed, but opening brackets remained in the stack, return the position of the first remaining opening bracket
    if len(opening_brackets_stack) > 0:
        # print('some opening brackets remained')
        return opening_brackets_stack[0].position

    return 'Success'



if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-06'

    parser = argparse.ArgumentParser(description='datastructures. check brackets in code',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--test', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.test:

        tests = {
                    '[]': 'Success',
                    '{}[]' : 'Success',
                    '(())': 'Success',
                    '{[]}()': 'Success',
                    '{': 1,
                    '{[}': 3,
                    'foo(bar)': 'Success',
                    'foo(bar[i);': 10,
                    '}': 1,
                }

        # run every test
        for text in tests.keys():

            print(text)

            # make timed call
            current_time1 = datetime.datetime.now()
            ret = check_brackets_in_code(text)
            current_time2 = datetime.datetime.now()
            
            if ret == tests[text]:
                print('result OK: ' + str(ret))
            else:
                print('result ERROR: ' + str(ret) + ' (should be ' + str(tests[text]) + ')')

            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        text = sys.stdin.read()
        print(check_brackets_in_code(text))



# original programming assignment

'''
### 1.1 Check Brackets In The Code

#### Problem Introduction
In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the
code.

#### Problem Description
**Task:** Your friend is making a text editor for programmers. He is currently working on a feature that will find errors in the usage of different types of brackets. Code can contain any brackets from the set []{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them are ],}, and.
For convenience, the text editor should not only inform the user that there is an error in the usage of brackets, but also point to the exact place in the code with the problematic bracket. First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like ] in ](), or closes the wrong opening bracket, like } in ()[}. If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of brackets is correct.
Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.
More formally, all brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c]. The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).

**Input Format:** Input contains one string *S* which consists of big and small latin letters, digits, punctuation marks and brackets from the set []{}().

**Constraints:** The length of *S* is at least 1 and at most 10^5.

**Output Format:** If the code in *S* uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.

**Time Limits:** C: 1 sec, C++: 1 sec, Java: 1 sec, Python: 1 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3 sec, Ruby: 3 sec, Scala: 3 sec.

**Memory Limit:** 512MB.

#### Sample 1

*Input:*
[]

*Output:*
Success
Explanation: The brackets are used correctly: there is just one pair of brackets [ and ], they correspond to each other, the left bracket [ goes before the right bracket ], and no two pairs of brackets intersect, because there is just one pair of brackets.

#### Sample 2

*Input:*
{}[]

*Output:*
Success
Explanation: The brackets are used correctly: there are two pairs of brackets — first pair of { and }, and second pair of [ and ] — and these pairs do not intersect.

#### Sample 3

*Input:*
[()]

*Output:*
Success
Explanation: The brackets are used correctly: there are two pairs of brackets — first pair of [ and ], and second pair of ( and ) — and the second pair is nested inside the first pair.

#### Sample 4

*Input:*
(())

*Output:*
Success
Explanation: Pairs with the same types of brackets can also be nested.

#### Sample 5

*Input:*
{[]}()

*Output:*
Success
Explanation: Here there are 3 pairs of brackets, one of them is nested into another one, and the third one is separate from the first two.

#### Sample 6

*Input:*
{

*Output:*
1
Explanation: The code { doesn’t use brackets correctly, because brackets cannot be divided into pairs (there is just one bracket). There are no closing brackets, and the first unmatched opening bracket is {, and its
position is 1, so we output 1.

#### Sample 7

*Input:*
{[}

*Output:*
3
Explanation: The bracket } is unmatched, because the last unmatched opening bracket before it is [ and not {. It is the first unmatched closing bracket, and our first priority is to output the first unmatched closing bracket, and its position is 3, so we output 3.

#### Sample 8

*Input:*
foo(bar);

*Output:*
Success
Explanation: All the brackets are matching, and all the other symbols can be ignored.

#### Sample 9

*Input:*
foo(bar[i);

*Output:*
10
Explanation: ) doesn’t match [, so ) is the first unmatched closing bracket, so we output its position, which is 10.

#### Implementation in Python

'''
