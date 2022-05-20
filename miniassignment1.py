from collections import Counter
from itertools import combinations


class StringClass:
    def __init__(self, value):
        self.str = value

    def length(self):
        return len(self.str)

    def tolist(self, value):
        list1 = list(value)
        return list1


class PairsPossible(StringClass):
    def __init__(self, value):
        self.str = value

    def pairs(self):
        pair = list(combinations(self.str, 2))
        return pair


class commonelement:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def common(self):
        dict1 = Counter(self.str1)
        dict2 = Counter(self.str2)
        commondict = dict1 & dict2
        commonchar = list(commondict.elements())
        print(commonchar)


class EqualSumPairs(PairsPossible):

    def UniqueSum(self):
        pairs = [[x, y] for x in self.str for y in self.str]
        Sum = []
        sum1 = 0
        for i in pairs:
            sum1 = int(i[0]) + int(i[1])
            Sum.append(sum)
            sum1 = 0
        uniqueList = []
        for x in Sum:
            if x not in uniqueList:
                uniqueList.append(x)
        print(len(uniqueList))


St = str(input("Enter String"))
ob = StringClass(St)
ob.length()
print(ob.length())
print(ob.tolist(St))
St2 = str(input("Enter Second String"))
o2 = PairsPossible(St2)
list1 = o2.pairs()
print("Pairs Possible are: ")
print(list1)
ob3 = commonelement(St, St2)
ob3.common()
ob4 = EqualSumPairs(St2)
ob4.UniqueSum()