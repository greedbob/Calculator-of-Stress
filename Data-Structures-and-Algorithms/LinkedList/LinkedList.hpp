//
// Created by greedbob on 19-3-3.
//

#ifndef PROJECT_LINKEDLIST_HPP
#define PROJECT_LINKEDLIST_HPP

struct Node{
    int data;
    Node * next;
};

class LinkedList {
public:
    LinkedList();
    void delList();
    void add(int num);
    void insert(int index, int num);
    void popList(int index = -1);
    int find(int num);
    bool isExist(int num);
    void reverse();
    void showList();
    int length;

private:
    Node * head;
    Node * tail;
};


#endif //PROJECT_LINKEDLIST_HPP
