//
// Created by greedbob on 19-3-5.
//
#include <assert.h>
#define DEBUG

template <typename T>
struct Node{
    T data;
    Node * next;
};

template <typename T>
class Stack {
public:
    Stack();
    bool isEmpty();
    void push(int value);
    T pop();
    T getTop();
    int getSize();

private:
    Node<T> * top = nullptr;
    int size = 0;
};

template <typename T>
Stack<T>::Stack()=default;

template <typename T>
bool Stack<T>::isEmpty(){
    if (top == nullptr) return false;
    else return true;
};

template <typename T>
void Stack<T>::push(int value) {
#ifndef DEBUG
    std::cout << "DEBUG_MESSAGE in Stack<T>::push: The value is: " << value << std::endl;
#endif
    Node<T> * node = new Node<T>;
    node->data = value;
    node->next = top;
    top = node;
    ++size;
};

template <typename T>
T Stack<T>::pop() {
    if (isEmpty()){
        Node<T> * node = top;
        T value = top->data;
        top = top->next;
        delete node;
        --size;
        return value;
    } else {
        assert("Error_Message in Stack<T>::pop()");
        exit(-1);
    }
};

template <typename T>
T Stack<T>::getTop() {
     if (isEmpty()) return top->data;
     else {
         assert("Error_Message in Stack<T>::getTop()");
         exit(-1);
     }
};

template <typename T>
int Stack<T>::getSize() {
    return size;
};