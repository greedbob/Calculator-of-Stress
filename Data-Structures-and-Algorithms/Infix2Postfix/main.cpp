#include <iostream>
#include "Stack.hpp"
#include "Infix2Postfix.hpp"
//#define DEBUG

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

void testInfix2Postfix(){
    std::string input;
    Stack<float> numStack;
    Stack<char> symStack;
    std::cout << "Please input the infix: " << std::endl;
    std::cin >> input;
    std::cout << "The input is: " << input << std::endl;

#ifdef DEBUG
    std::cout << "Is the numStack empty? " << numStack.isEmpty() << std::endl;
    std::cout << "Is the symStack empty? " << symStack.isEmpty() << std::endl;
    std::cout << "Test the input and isNum(): " << std::endl;
    for (int j = 0; j < input.size(); ++j) {
        std::cout << "The #" << j << " char is: " << input[j] << " ";
        std::cout << "Is num? " << isNum(input[j]) << std::endl;
    }
    std::cout << "Test the isPriority(): " << isPriority('+', '*') << " "
        << isPriority('/', '-') << " " << isPriority('(', '+') << " " << isPriority(')', '*') << std::endl;
#endif

    std::string output = transferProcess(input, symStack);
    std::cout << "The Postfix is: " << output << std::endl;

    float ans = solvePostfix(output, numStack);
    std::cout << "The answer is: " << ans << std::endl;
}

int main() {
    // 测试后缀转中缀并计算
    testInfix2Postfix();
    return 0;
}