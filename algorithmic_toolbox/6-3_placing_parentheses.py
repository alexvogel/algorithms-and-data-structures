# Uses python3
import argparse
import random
import sys
import datetime

# evaluate a term
def evalt(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

# calc the min and max of the given subterm
def MinAndMax(matrix_min, matrix_max, i, j, operations):

    # init min/max
    myMin = float("inf")
    myMax = float("-inf")

    for k in range(i, j):

        # print('M(i,k)=M(' + str(i) + ', ' + str(k) + ') => ' + str(matrix_max[i][k])) 
        # print('m(i,k)=M(' + str(i) + ', ' + str(k) + ') => ' + str(matrix_min[i][k])) 
        # print('M(k+1,j)=M(' + str(k+1) + ', ' + str(j) + ') => ' + str(matrix_max[k+1][j])) 
        # print('m(k+1,j)=M(' + str(k+1) + ', ' + str(j) + ') => ' + str(matrix_min[k+1][j])) 
        # print('operation: ' + operations[i])

        a = evalt(matrix_max[i][k], matrix_max[k+1][j], operations[k])
        b = evalt(matrix_max[i][k], matrix_min[k+1][j], operations[k])
        c = evalt(matrix_min[i][k], matrix_max[k+1][j], operations[k])
        d = evalt(matrix_min[i][k], matrix_min[k+1][j], operations[k])

        # print('calc_the_min_of: ' + str(myMin), str(a), str(b), str(c), str(d))

        myMin = min([myMin, a, b, c, d])
        myMax = max([myMax, a, b, c, d])

    # print('myMin: ' + str(myMin))
    # print('myMax: ' + str(myMax))

    return (myMin, myMax)

# set the parentheses to maximize the result of the expression
def Parentheseses(dataset, solutiontable=False):

    len_dataset = len(dataset)

    # for i in range (0, len(dataset)):
    #     print(str(i) + ': ' + dataset[i])

    numbers = []
    operations = []

    for i in range(0, len_dataset):
        
        if i % 2 != 0:
            operations.append(dataset[i])
        else:
            numbers.append(int(dataset[i]))

    len_numbers = len(numbers)

    # create min and max matrices
    # amount of rows = amount of columns = amount of numbers
    matrix_min = [[None] * (len_numbers) for i in range(len_numbers)]
    matrix_max = [[None] * (len_numbers) for i in range(len_numbers)]

    # fill the diagonal with the numbers
    for i in range(0, len_numbers):
        matrix_min[i][i] = numbers[i]
        matrix_max[i][i] = numbers[i]

    for s in range(1, len_numbers):
        for i in range(0, len_numbers - s):


            j = i+s

            # print('i=' + str(i))
            # print('j=' + str(j))
            matrix_min[i][j], matrix_max[i][j] = MinAndMax(matrix_min, matrix_max, i, j, operations)

            if solutiontable:
                # print('matrix MIN values')
                for row in matrix_min:
                    print(row)
                # print('matrix MAX values')
                for row in matrix_max:
                    print(row)

    if solutiontable:
        print('matrix MIN values')
        for row in matrix_min:
            print(row)
        print('matrix MAX values')
        for row in matrix_max:
            print(row)

        # reconstructing the setting of parentheses from the solutiontable


    # return the largest possible solution for all possible settings of parentheses
    return matrix_max[0][len_numbers-1]

if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-05'

    parser = argparse.ArgumentParser(description='Maximum Value of an Arithmetic Expression',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--solutiontable', action='store_true',
                       help='print the solution table along with the result')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(4, 4)

            # numbers
            numbers = []

            # generate numbers
            for i in range(0, n):
                numbers.append(random.randint(1, 9))

            operations = []
            # generate operetions
            for i in range(0, n-1):
                operation_id = random.randint(1, 3)

                if operation_id == 1:
                    operations.append('+')
                elif operation_id == 2:
                    operations.append('-')
                elif operation_id == 3:
                    operations.append('*')
                else:
                    print('ERROR: operation id ' + str(operation_id) + ' not possible')
                    sys.exit(1)

            # create dataset with first number
            dataset = [numbers.pop(0)]

            #
            for i in range(0, len(numbers)):
                dataset.append(operations[i])
                dataset.append(numbers[i])

            dataset_as_string = ''.join(str(e) for e in dataset)
            print(dataset_as_string)

            # make timed call
            current_time1 = datetime.datetime.now()
            largestPossibleNumber = Parentheseses(dataset_as_string, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(largestPossibleNumber))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        if args.solutiontable:
            print(Parentheseses(input(), solutiontable=True))
        else:
            print(Parentheseses(input(), solutiontable=False))
