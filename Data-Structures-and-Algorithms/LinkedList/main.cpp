//
// Created by greedbob on 19-3-3.
//

#include "LinkedList.hpp"
#include <iostream>

int main(){
    LinkedList linkedList;

    // Test add numbers
    for (int i = 0; i < 10; ++i) {
        linkedList.add(i);
    }
    linkedList.showList();

    // Test insert numbers
    linkedList.insert(0, 100);
    linkedList.insert(5, 200);
    linkedList.insert(-1, 300);
    linkedList.showList();

    //Test exist and find
    int testNum = 300;
    bool exist = linkedList.isExist(testNum);
    if (exist){
        std::cout << "The number " << testNum << " is exist." << std::endl;
        int index = linkedList.find(testNum);
        std::cout << "The index of " << testNum << " is " << index << "." << std::endl;
    } else{
        std::cout << "The number " << testNum << " is not exist." << std::endl;
    }

    //Test pop numbers
    linkedList.popList(0);
    linkedList.popList();
    linkedList.popList(4);
    linkedList.showList();

    //Test reverse list
    linkedList.reverse();
    linkedList.showList();

    //Test delete list
    linkedList.delList();
    std::cout << "The length of list is: " << linkedList.length << std::endl;
}

