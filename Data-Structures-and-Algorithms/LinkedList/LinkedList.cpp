//
// Created by greedbob on 19-3-3.
//

#include "LinkedList.hpp"
#include <iostream>
#define DEBUG

LinkedList::LinkedList(){
    Node * node = new Node;
    head = node;
    tail = node;
    node->next = nullptr;
    length = 0;
};

void LinkedList::add(int num){
    if (length > 0){
        Node * temp = new Node;
        temp->data = num;
        temp->next = nullptr;
        tail->next = temp; //point to last in present
        tail = temp;
    } else{
        head->data = num;
    }
    length++;
}

void LinkedList::delList(){
    if (length <= 0){
        std::cout << "delList Error." <<std::endl;
    }else {
        while (head != tail) {
            Node * temp = head->next;
            delete head;
            head = temp;
            --length;
        }
        delete (head);
        --length;
    }
};

void LinkedList::insert(int index, int num){
    if (index < 0){
        if (index + length > 0){
            index = index + length + 1;
        } else{
            std::cout << "#1 insert Error." << std::endl;
            return;
        }
    }
    if (index == 0){
        Node * temp = new Node;
        temp->next = head;
        temp->data = num;
        head = temp;
    } else if (index <= length){
        Node * temp = head;
        for (int i = 0; i < index - 1; ++i, temp = temp->next){}
        Node * node = new Node;
        node->data = num;
        node->next = temp->next;
        temp->next = node;
        if (index == length){
            tail = node;
        }
    } else {
        std::cout << "#2 insert Error." << std::endl;
        return;
    }
    ++length;
#ifndef DEBUG
    std::cout << "Debug Message: length is " << length << std::endl;
#endif
};

void LinkedList::popList(int index){
    if (index < 0){
        if (index + length > 0){
            index = index + length;
        } else{
            std::cout << "#1 popList Error." << std::endl;
            return;
        }
    }
    if (index == 0){
        Node * cur = head;
        head = head->next;
        delete cur;
    } else if (index >0 && index <= length){
        Node * pre = head;
        for (int i = 0; i < index - 1; ++i, pre = pre->next) {}
#ifndef DEBUG
        std::cout << "Debug Messages: pre->data is " << pre->data << std::endl;
#endif
        Node * cur = pre->next;
        pre->next = cur->next;
        delete cur;
        if (index == length - 1) tail = pre;
    } else {
        std::cout << "#2 popList Error." << std::endl;
        return;
    }
    --length;
#ifndef DEBUG
    std::cout << "Debug Messages: tail->data is " << tail->data << std::endl;
#endif
};

int LinkedList::find(int num){
    Node * cur = head;
    for (int index = 0; index < length; ++index, cur = cur->next){
        if (cur->data == num) return index;
    }
    return -1;
};

bool LinkedList::isExist(int num){
    Node * cur = head;
    for (int index = 0; index < length; ++index, cur = cur->next){
        if (cur->data == num) return true;
    }
    return false;
};

void LinkedList::reverse(){

    Node * pre = head;
    Node * cur = head->next;
    Node * nex = cur->next;

    Node * odlHead = head;
#ifndef DEBUG
    std::cout << "Debug Message: The head->data is " << head->data << std::endl;
    std::cout << "Debug Message: The tail->data is " << tail->data << std::endl;
#endif
    head = tail;
    tail = odlHead;
#ifndef DEBUG
    std::cout << "Debug Message: The head->data is " << head->data << std::endl;
    std::cout << "Debug Message: The tail->data is " << tail->data << std::endl;
#endif
    pre->next = nullptr;
    for (int i = 1; i < length; ++i) {
        cur->next = pre;
        pre = cur;
        cur = nex;
        if (i < length - 1) nex = nex->next;
    }
#ifndef DEBUG
    std::cout << "Debug Message: The head->data is " << head->data << std::endl;
    std::cout << "Debug Message: The tail->data is " << tail->data << std::endl;
#endif
};

void LinkedList::showList(){
    Node * cur = head;
    std::cout << "The Linked List is: ";
    if (length > 0){
        for (int i = 0; i < length; ++i, cur = cur->next) {
            std::cout << cur->data << " ";
        }
    }
    std::cout << std::endl;
};