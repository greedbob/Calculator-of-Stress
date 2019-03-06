#include <iostream>
#include "Stack.hpp"
#include "TestStack.hpp"
#include "Infix2Postfix.hpp"

int main() {
    Stack<int> stack;
    TestStack(stack);

    Infix2Postfix();

    return 0;
}