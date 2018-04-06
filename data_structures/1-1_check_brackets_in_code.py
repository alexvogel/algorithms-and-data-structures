# Uses python3
import argparse
import random
import sys
import datetime

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
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
            opening_brackets_stack.append(i)

        # if the current character is a closing bracket
        if character == ')' or character == ']' or character == '}':

            if len(opening_brackets_stack) == 0:
                return i+1

            matchBracket = None
            
            if character == ')':
                matchBracket = '('

            elif character == ']':
                matchBracket = '['

            elif character == '}':
                matchBracket = '{'

            else:
                print('ERROR')
                sys.exit(1)

            # if last opening bracket matches the closing bracket, remove the opening bracket from stack
            if text[opening_brackets_stack[-1]] == matchBracket:
                # print('closing bracket fits last opening bracket')
                # print('last opening bracket was ' + str(text[opening_brackets_stack[-1]]))
                opening_brackets_stack.pop()

            # if the last opening bracket does not match the closing bracket, return current position
            else:
                # print('closing bracket does not fit last opening bracket')
                # print('last opening bracket was ' + str(text[opening_brackets_stack[-1]]))
                return i+1

    # if whole text has been processed, but opening brackets remained in the stack, return the position of the first remaining opening bracket
    if len(opening_brackets_stack) > 0:
        # print('some opening brackets remained')
        return opening_brackets_stack[0] + 1

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
