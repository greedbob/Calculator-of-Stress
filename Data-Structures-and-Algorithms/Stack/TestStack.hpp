//
// Created by greed on 2019/3/6.
//

#include <iostream>

template <typename T>
void TestStack(Stack<T> stack){
    //isEmpty()
    std::cout << "Test isEmpty()" << std::endl;
    std::cout << "The stack is empty? " << (stack.isEmpty() ? "NO" : "YES") << std::endl;
    std::cout << "The size of stack is " << stack.getSize() <<std::endl;

    //push()
    std::cout << "Test push()" << std::endl;
    stack.push(0);
    stack.push(1);
    stack.push(2);
    std::cout << "The top of stack is " << stack.getTop() << std::endl;
    int size = stack.getSize();
    std::cout << "The size of stack is " << stack.getSize() << std::endl;

    //pop()
    std::cout << "Test pop()" << std::endl;
    std::cout << "The stack is:";
    for (int i = 0; i < size; ++i) {
        std::cout << " " << stack.pop();
    }
    std::cout << std::endl;
}