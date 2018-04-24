# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):

        self.myHash = Hash(bucket_count, self._multiplier, self._prime)

        #self.bucket_count = bucket_count
        # store all strings in one list
        #self.elems = []

    # def _hash_func(self, s):
    #     ans = 0
    #     for c in reversed(s):
    #         ans = (ans * self._multiplier + ord(c)) % self._prime
    #     return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())


    def process_query(self, query):
        if query.type == "check":

            self.write_chain(self.myHash.getKeyListOfCertainHashValue(query.ind))

        else:
            if query.type == 'find':
                self.write_search_result(self.myHash.hasKey(query.s))

            elif query.type == 'add':
                self.myHash.set(query.s, 'blub')
            elif query.type == 'del':
                self.myHash.remove(query.s)



    def process_query_(self, query):


        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)


        print(self.elems)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


class Hash:
    def __init__(self, cardinality, multiplier, prime):
        self.cardinality = cardinality
        self.multiplier = multiplier
        self.prime = prime
        self.A = [None] * self.cardinality

#        for i in range(0, self.cardinality):
#            self.A.append([])

    def calcHash_int(self, key):
        #print(str(key) + ' => hashValue of ' + str(int(key) % self.cardinality))
        return int(key) % self.cardinality

    def calcHash(self, string):
        ans = 0
        for c in reversed(string):
            ans = (ans * self.multiplier + ord(c)) % self.prime
        return ans % self.cardinality


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

    def getKeyListOfCertainHashValue(self, hashValue):

        if self.A[hashValue] == None:
            return ''

        keys = []

        for key_value_pair in self.A[hashValue]:
            keys.append(key_value_pair[0])

        return list(reversed(keys))

    def remove(self, key):

        hashValue = self.calcHash(key)

        if self.A[hashValue] == None:
            return

        for i in range(0, len(self.A[hashValue])):
            if self.A[hashValue][i][0] == key:
                del self.A[hashValue][i]
                return


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

'''
### 4.2 Hashing with chains

#### Problem Introduction
In this problem you will implement a hash table using the chaining scheme. Chaining is one of the most popular ways of implementing hash tables in practice. The hash table you will implement can be used to implement a phone book on your phone or to store the password table of your computer or web service (but don’t forget to store hashes of passwords instead of the passwords themselves, or you will get hacked!).

#### Problem Description
**Task:** In this task your goal is to implement a hash table with lists chaining. You are already given the number of buckets m and the hash function. It is a polynomial hash function
⎛
⎞
|S|−1
∑︁
h(S) = ⎝
S[i]x i mod p ⎠ mod m ,
i=0
where S[i] is the ASCII code of the i-th symbol of S, p = 1000000007 and x = 263. Your program should support the following kinds of queries:  
∙ add string — insert string into the table. If there is already such string in the hash table, then just ignore the query.  
∙ del string — remove string from the table. If there is no such string in the hash table, then just ignore the query.  
∙ find string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.  
∙ check i — output the content of the i-th list in the table. Use spaces to separate the elements of the list. If i-th list is empty, output a blank line.  
When inserting a new string into a hash chain, you must insert it in the beginning of the chain.  
**Input Format:** There is a single integer m in the first line — the number of buckets you should have. The next line contains the number of queries N . It’s followed by N lines, each of them contains one query in the format described above.
**Constraints:** 1 ≤ N ≤ 10^5 ; N/5 ≤ m ≤ N . All the strings consist of latin letters. Each of them is non-empty and has length at most 15.  
**Output Format:** Print the result of each of the find and check queries, one result per line, in the same order as these queries are given in the input.  
**Time Limits:** C: 1 sec, C++: 1 sec, Java: 5 sec, Python: 7 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 7 sec, Ruby: 7 sec, Scala: 7 sec.  
**Memory Limit:** 512Mb.  

#### Sample 1

*Input:*  
5  
12  
add world  
add HellO  
check 4  
find World  
find world  
del world  
check 4  
del HellO  
add luck  
add GooD  
check 2  
del good  

*Output:*  
HellO world  
no  
yes  
HellO  
GooD luck  
**Explanation:**  
The ASCII code of ’w’ is 119, for ’o’ it is 111, for ’r’ it is 114, for ’l’ it is 108, and for ’d’ it is 100. Thus, h(“world") = (119 + 111 × 263 + 114 × 263 2 + 108 × 263 3 + 100 × 263 4 mod 1 000 000 007) mod 5 = 4. It turns out that the hash value of HellO is also 4. Recall that we always insert in the beginning of the chain, so after adding “world" and then “HellO" in the same chain index 4, first goes “HellO" and then goes “world". Of course, “World" is not found, and “world" is found, because the strings are case-sensitive, and the codes of ’W’ and ’w’ are different. After deleting “world", only “HellO" is found in the chain 4. Similarly to “world" and “HellO", after adding “luck" and “GooD" to the same chain 2, first goes “GooD" and then “luck".

#### Sample 2

*Input:*  
4  
8  
add test  
add test  
find test  
del test  
find test  
find Test  
add Test  
find Test  

*Output:*  
yes  
no  
no  
yes  
**Explanation:**  
Adding “test" twice is the same as adding “test" once, so first find returns “yes". After del, “test" is no longer in the hash table. First time find doesn’t find “Test” because it was not added before, and strings are case-sensitive in this problem. Second time “Test” can be found, because it has just been added.

#### Sample 3

*Input:*  
3  
12  
check 0  
find help  
add help  
add del  
add add  
find add  
find del  
del del  
find del  
check 0  
check 1  
check 2  

*Output:*  
no  
yes  
yes  
no  
add help  
**Explanation:**  
Note that you need to output a blank line when you handle an empty chain. Note that the strings stored in the hash table can coincide with the commands used to work with the hash table.  

#### What to Do
Follow the explanations about the chaining scheme from the lectures. Remember to always insert new strings in the beginning of the chain. Remember to output a blank line when check operation is called on an empty chain.

#### Some hints based on the problems encountered by learners:
∙ Beware of integer overflow. Use long long type in C++ and long type in Java where appropriate. Take everything (mod p) as soon as possible while computing something (mod p), so that the numbers are always between 0 and p − 1.  
∙ Beware of taking negative numbers (mod p). In many programming languages, (−2)%5 ̸ = 3%5. Thus you can compute the same hash values for two strings, but when you compare them, they appear to be different. To avoid this issue, you can use such construct in the code: x ← ((a%p) + p)%p instead of just x ← a%p.

#### Implementation in Python

[4-2_hash_chains.py](4-2_hash_chains.py)
'''
