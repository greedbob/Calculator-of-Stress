from collections import *


def main():
    minsup = 2
    maxLen, itemsets, trans = testInput()
    # maxLen, itemsets, trans = inputTrans()
    sortedTrans = sortTrans(trans)
    itemsets = apriori(minsup, maxLen, itemsets, sortedTrans)
    print('Final Dict:')
    for dict in itemsets:
        print(dict)
    return 0


def testInput():
    maxLen = 4
    itemsets = [OrderedDict([('1', 0), ('2', 0), ('3', 0), ('4', 0)])]
    trans = [['1'], ['1', '2'], ['1', '2', '3'], ['1', '2', '3', '4'], ['1', '2', '3', '4']]
    return maxLen, itemsets, trans


def inputTrans():
    maxLen = 0
    trans = []
    dict = OrderedDict()
    items = [dict]
    line = ' '
    while (line):
        line = input('Enter the trans: ').strip()
        if line:
            tran = []
            for item in line.split(' '):
                tran.append(item)
                if item not in items[0]: items[0][item] = 0
            if len(tran) > maxLen: maxLen = len(tran)
            trans.append(tran)
    return maxLen, items, trans


def sortTrans(trans):
    sortedTrans = []
    for tran in trans:
        if len(sortedTrans) == 0:
            sortedTrans.append(tran)
        else:
            index = 0
            inserted = False
            while index < len(sortedTrans):
                if len(tran) < len(sortedTrans[index]):
                    sortedTrans.insert(index, tran)
                    inserted = True
                    break
                index += 1
            if not inserted: sortedTrans.append(tran)
    return sortedTrans


def apriori(minsup, maxLen, itemsets, sortedTrans):
    for index in range(maxLen):
        print('#', index, )
        itemset = itemsets[index]
        # calculate the support of itemset
        for key in itemset.keys():
            for tran in sortedTrans:
                isIn = True
                for str in key:
                    if str not in tran: isIn = False
                if isIn: itemset[key] += 1
        print('calculate the support of itemset: ', itemset)
        # delete the infrequent itemset
        print('itemset.keys(): ', itemset.keys())
        keylist = list(itemset.keys())
        for key in keylist:
            if itemset[key] < minsup: itemset.pop(key)
        print('delete the infrequent itemset: ', itemset)
        if len(itemset) == 0:
            break
        else:
            newitemset = OrderedDict()
            keylist = list(itemset.keys())
            print('keylist', keylist)
            for i in range(len(keylist)):
                for j in range(i + 1, len(keylist)):
                    print('i: ', i, 'j: ', j)
                    if keylist[i][:-1] == keylist[j][:-1] and keylist[i][-1] != keylist[j][-1]:
                        newKey = keylist[i] + keylist[j][-1]
                        newitemset[newKey] = 0
            itemsets.append(newitemset)
            print('itemsets: ', itemsets)
    return itemsets


if __name__ == '__main__':
    main()