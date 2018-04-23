# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []

    phoneBook = PhoneBook()

    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name

            phoneBook.set(cur_query.number, cur_query.name)

        elif cur_query.type == 'del':
            phoneBook.deleteByNumber(cur_query.number)

        else:
            result.append(phoneBook.findByNumber(cur_query.number))

    return result


class PhoneBook:
    def __init__(self):
        #self.phoneBookByName = Hash()
        self.phoneBookByNumber = Hash()

    def set(self, number, name):
        #self.phoneBookByName.set(name, number)
        self.phoneBookByNumber.set(number, name)

    def deleteByNumber(self, number):
        if self.phoneBookByNumber.hasKey(number):
            #name = self.phoneBookByNumber.get(number)
            self.phoneBookByNumber.remove(number)
            #self.phoneBookByName.remove(name)

    def findByNumber(self, number):
        return self.phoneBookByNumber.get(number)

    def existNumber(self, number):
        return self.phoneBookByNumber.hasKey(number)



class Hash:
    def __init__(self):
        self.cardinality = 10000000
        self.A = [None] * self.cardinality

#        for i in range(0, self.cardinality):
#            self.A.append([])

    def calcHash(self, key):
        #print(str(key) + ' => hashValue of ' + str(int(key) % self.cardinality))
        return int(key) % self.cardinality

    def set(self, key, value):

        # calc the hash value from the key
        hashValue = self.calcHash(key)

        didSet = False

        if self.A[hashValue] == None:
            self.A[hashValue] = []
            self.A[hashValue].append([key, value])
            didSet = True

        # iterate over all key_value pairs that are stored under the list position #hashValue
        else:
            for i in range (0, len(self.A[hashValue])):

                # if key already exists, reset value
                if self.A[hashValue][i][0] == key:
                    self.A[hashValue][i][1] = value
                    didSet = True

        # in case of chaining
        if not didSet:
            key_value_pair = [key, value]
            self.A[hashValue].append(key_value_pair)


    def hasKey(self, key):

        # calc the hash value from the key
        hashValue = self.calcHash(key)

        if self.A[hashValue] == None:
            return False


        # iterate over all key_value pairs that are stored under the list position #hashValue
        for key_value_tuple in self.A[hashValue]:


            # if key is found -> True
            if key_value_tuple[0] == key:
                return True

        # if key is not found -> False
        return False

    def get(self, key):

        hashValue = self.calcHash(key)

        if self.A[hashValue] == None:
            return 'not found'

        for key_value_pair in self.A[hashValue]:
            if key_value_pair[0] == key:
                return key_value_pair[1]

        return 'not found'

    def remove(self, key):

        hashValue = self.calcHash(key)

        for i in range(0, len(self.A[hashValue])):
            #print('i='+str(i) + '  ' + str(self.A[hashValue][i]))
            if self.A[hashValue][i][0] == key:
                del self.A[hashValue][i]


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

'''
### 4.1 Phone book

#### Problem Introduction
In this problem you will implement a simple phone book manager.

#### Problem Description
**Task:** In this task your goal is to implement a simple phone book manager. It should be able to process the following types of user’s queries:   ∙ add number name. It means that the user adds a person with name name and phone number number to the phone book. If there exists a user with such number already, then your manager has to overwrite the corresponding name.   ∙ del number. It means that the manager should erase a person with number number from the phone book. If there is no such person, then it should just ignore the query.   ∙ find number. It means that the user looks for a person with phone number number. The manager should reply with the appropriate name, or with string “not found" (without quotes) if there is no such person in the book.  
**Input Format:** There is a single integer N in the first line — the number of queries. It’s followed by N lines, each of them contains one query in the format described above.  
**Constraints:** 1 ≤ N ≤ 10^5 . All phone numbers consist of decimal digits, they don’t have leading zeros, and each of them has no more than 7 digits. All names are non-empty strings of latin letters, and each of them has length at most 15. It’s guaranteed that there is no person with name “not found".   
**Output Format:** Print the result of each find query — the name corresponding to the phone number or “not found" (without quotes) if there is no person in the phone book with such phone number. Output one result per line in the same order as the find queries are given in the input.  
**Time Limits:** C: 3 sec, C++: 3 sec, Java: 6 sec, Python: 6 sec. C#: 4.5 sec, Haskell: 6 sec, JavaScript: 9 sec, Ruby: 9 sec, Scala: 9 sec.  
**Memory Limit:** 512Mb.

#### Sample 1

*Input:*  
12  
add 911 police  
add 76213 Mom  
add 17239 Bob  
find 76213  
find 910  
find 911  
del 910  
del 911  
find 911  
find 76213  
add 76213 daddy  
find 76213  

*Output:*  
Mom  
not found  
police  
not found  
Mom  
daddy  
**Explanation:**  
76213 is Mom’s number, 910 is not a number in the phone book, 911 is the number of police, but then it was deleted from the phone book, so the second search for 911 returned “not found". Also, note that when the daddy was added with the same phone number 76213 as Mom’s phone number, the contact’s name was rewritten, and now search for 76213 returns “daddy" instead of “Mom".

#### Sample 2

*Input:*  
8  
find 3839442  
add 123456 me  
add 0 granny  
find 0  
find 123456  
del 0  
del 0  
find 0  

*Output:*  
not found  
granny  
me  
not found  
**Explanation:**  
Recall that deleting a number that doesn’t exist in the phone book doesn’t change anything.

#### Implementation in Python

[4-1_phone_book.py](4-1_phone_book.py)
'''
