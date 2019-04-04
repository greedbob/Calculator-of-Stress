# Code by Bo in April 2019 for Data Mining Course
def main():
    minsup = 2
    # use testInput() function to get data directly without input
    # maxLen, itemsets, supports, trans = testInput()
    # use inputTrans() to input data
    maxLen, itemsets, supports, trans = inputTrans()
    sortedTrans = sortTrans(trans)
    itemsets, supports = apriori(minsup, maxLen, itemsets, supports, sortedTrans)
    output(itemsets, supports)
    return 0


def testInput():
    maxLen = 4
    itemsets = [[['1'], ['2'], ['3'], ['4'], ['5']]]
    supports = [[0, 0, 0, 0, 0]]
    trans = [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5'], ['1', '2', '3', '5']]
    return maxLen, itemsets, supports, trans


def inputTrans():
    maxLen = 0
    trans = []
    itemsets = [[]]
    supports = [[]]
    line = ' '
    while (line):
        line = input('Enter the trans: ').strip()
        if line:
            tran = []
            for index, item in enumerate(line.split(' ')):
                tran.append(item)
                if [item] not in itemsets[0]:
                    itemsets[0].append([item])
                    supports[0].append(0)
            if len(tran) > maxLen:
                maxLen = len(tran)
            trans.append(tran)
    print(itemsets)
    print(supports)
    print(trans)
    return maxLen, itemsets, supports, trans


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


def apriori(minsup, maxLen, itemsets, supports, sortedTrans):
    for index in range(maxLen):
        print('#', index, )
        itemset = itemsets[index]
        support = supports[index]
        if not itemset:
            break
        else:
            # calculate the support of itemset
            for index_items, items in enumerate(itemset):
                for tran in sortedTrans:
                    isIn = True
                    for item in items:
                        if item not in tran:
                            isIn = False
                    if isIn:
                        support[index_items] += 1
            print('After calculate the support of itemset: {0} support: {1}'.format(itemset, support))
            # delete the infrequent itemset
            for index_key, key in enumerate(itemset):
                if support[index_key] < minsup:
                    itemset.pop(index_key)
                    support.pop(index_key)
            print('After delete the infrequent itemset: {0} support: {1}'.format(itemset, support))
            # generate new itemset
            new_itemset = []
            new_support = []
            for i in range(len(itemset)):
                for j in range(i + 1, len(itemset)):
                    if itemset[i][:-1] == itemset[j][:-1] and itemset[i][-1] != itemset[j][-1]:
                        new_items = itemset[i].copy()
                        new_items.append(itemset[j][-1])
                        new_itemset.append(new_items)
                        new_support.append(0)
            print('After generate new itemsets: {0} support: {1}'.format(itemset, support))
            itemsets.append(new_itemset)
            supports.append(new_support)
            print('Finish # {0}: itemsets: {1} supports: {2}'.format(index, itemsets, supports))
    return itemsets, supports


def output(itemsets, supports):
    print('Final Result:')
    for index, itemset in enumerate(itemsets):
        for index_items, items in enumerate(itemset):
            line = ''
            for item in items:
                line += item
                line += ' '
            print('{0} #SUP: {1}'.format(line, supports[index][index_items]))


if __name__ == '__main__':
    main()
