# Uses python3
import argparse
import random
import sys
import datetime
import math


def optimal_sequence_dynamic_programming(n):
    # define possible denominations
    operations = ['mult2', 'mult3', 'add1']

    # create a list for the count
    T = [math.inf] * (n + 1)

    # the first number is 0
    # this definition is important, because all other calculations base on this number
    T[0] = 0
    T[1] = 0

    # create a list for the used operations
    R = [-1] * (n + 1)

    # loop over exist operation types
    for i in range(1, len(T)):
        #print('i=' + str(i))

        # loop over every number between 1 and the goal
        for j in range(0, len(operations)):
            #print('     operation=' + operations[j])

            # if operation is mult3 and
            # i is devidable by 3, check if going from T[i//3] would lead to a lesser number of operations
            if operations[j] == 'mult3' and i % 3 == 0:
                #print('     mult3')


                tillNow = T[i]

                #print('         tillNow=' + str(T[i]))
                T[i] = min(T[i], 1 + T[i // 3])
                #print('         after=' + str(T[i]))

                # if it lead to a lesser number of operations, enter the operations index into the list of operations
                if tillNow != T[i]:
                    R[i] = j

            # the same for mult2
            if operations[j] == 'mult2' and i % 2 == 0:
                #print('     mult2')

                tillNow = T[i]

                #print('         tillNow=' + str(T[i]))
                T[i] = min(T[i], 1 + T[i // 2])
                #print('         after=' + str(T[i]))

                if tillNow != T[i]:
                    R[i] = j

            # the same for add1
            if operations[j] == 'add1' and i > 0:
                #print('     add1')

                tillNow = T[i]

                #print('         tillNow=' + str(T[i]))
                T[i] = min(T[i], 1 + T[i - 1])
                #print('         after=' + str(T[i]))

                if tillNow != T[i]:
                    R[i] = j

    # for debugging purposes, create a list with the needed operations
    # create the sequence of operations
    needed_operations = []

    for index in R:

        if index is -1:
            needed_operations.append(None)
        else:
            needed_operations.append(operations[index])

    # for debugging
    #print('needed operations=' + str(needed_operations))

    # create the sequence of visited numbers
    sequence = []

    # start at the resulting number and perform the operations on the numbers visited
    # till one reach number 1
    number = n
    while number > 1:

        sequence.append(number)

        if needed_operations[number] == 'mult3':
            number = number // 3

        elif needed_operations[number] == 'mult2':
            number = number // 2

        elif needed_operations[number] == 'add1':
            number = number - 1

        else:
            print('ERROR')

    # the first number is the 1
    sequence.append(1)

    # reverse the list to bring it in the right order
    sequence = list(reversed(sequence))

    return sequence

# the greedy solution does not return the optimal solution - only the dynamic programming solution does.
def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-31'

    parser = argparse.ArgumentParser(description='dynamic programming - primitive calculator',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--greedy', action='store_true',
                       help='use the greedy algorithm')
    parser.add_argument('--dp', action='store_true',
                       help='use the dynamic programming algorithm')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 3)
            print(n)

            current_time1 = datetime.datetime.now()
            res = optimal_sequence_dynamic_programming(n)
            current_time2 = datetime.datetime.now()
            
            print('result: ', end=' ')

            for number in res:
                print(number, end=' ')
            print()
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    elif args.greedy:
        input = sys.stdin.read()
        n = int(input)
        sequence = list(optimal_sequence_greedy(n))
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')

    elif args.dp:
        input = sys.stdin.read()
        n = int(input)
        sequence = list(optimal_sequence_dynamic_programming(n))
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        n = int(input)
        sequence = list(optimal_sequence_dynamic_programming(n))
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')
