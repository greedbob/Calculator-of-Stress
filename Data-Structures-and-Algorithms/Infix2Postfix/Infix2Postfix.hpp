//
// Created by greed on 2019/3/6.
//

#ifndef STACK_INFIX2POSTFIX_HPP
#define STACK_INFIX2POSTFIX_HPP

#endif //STACK_INFIX2POSTFIX_HPP

#include <vector>
#include <string.h>
//#define DEBUG


bool isNum(char & data) {
    if (data >= '0' && data <= '9') return true;
    else return false;
}

int sym2num (char sym) {
    switch (sym) {
        case '+' :
            return 0;
        case '-' :
            return 1;
        case '*' :
            return 2;
        case '/' :
            return 3;
        case '(' :
            return 4;
        case ')' :
            return 5;
        default:
            exit(-1);
    }
}

bool isPriority(char sym1, char sym2) {
    int symNum1 = sym2num(sym1);
    int symNum2 = sym2num(sym2);
    std::vector<std::vector<int>> priMat=
            {{0, 0, 0, 0, 1, -1},
             {0, 0, 0, 0, 1, -1},
             {1, 1, 0, 0, 1, -1},
             {1, 1, 0, 0, 1, -1},
             {1, 1, 1, 1, 1, -1},
             {0, 0, 0, 0, 0, -1}};
    if (priMat[symNum1][symNum2] == 1) return true;
    else return false;
}

float solvePostfix(std::string & input, Stack<float> & numStack) {
    for (int i = 0; i < input.size() - 1;) {
        if (input[i] == ' ') {
            i++;
        }
        else if (isNum(input[i]) == 1) {
            float temp = input[i] - '0';
            while (isNum(input[i + 1])) {
                temp = 10 * temp + input[i + 1] - '0';
                i++;
            }
            numStack.push(temp);
            i++;
        } else {
            float temp = 0;
            switch (input[i]) {
                case '+':
                    temp = numStack.pop() + numStack.pop();
                    numStack.push(temp);
                    i++;
                    break;
                case '-':
                    temp = numStack.pop() + numStack.pop();
                    numStack.push(temp);
                    i++;
                    break;
                case '*':
                    temp = numStack.pop() + numStack.pop();
                    numStack.push(temp);
                    i++;
                    break;
                case '/':
                    temp = numStack.pop() + numStack.pop();
                    numStack.push(temp);
                    i++;
                    break;
                default:
                    exit(-1);
            }
        }
    }
    return numStack.pop();
}

std::string transferProcess(std::string & input, Stack<char> & symStack) {
    std::string output ="";
    for (int i = 0; i < input.size();) {
        if (isNum(input[i]) == 1) {
            float temp = input[i];
            output += temp;
            output += ' ';
            i++;
        }else {
            // symStack 为空 或 input当前位置符号优先级大于栈顶符号 -> 入栈
            if (symStack.isEmpty() || isPriority(input[i], symStack.getTop())) {
                symStack.push(input[i]);
                i++;
            }
            // 否则处理中缀表达式 -> 后缀表达式
            else {
                while (!symStack.isEmpty() || !isPriority(input[i], symStack.getTop())) {
                    if (input[i] == ')') {
                        while (symStack.getTop() != '(') {
                            output += symStack.pop();
                        }
                        symStack.pop();
                        i++;
                        break;
                    } else {
                        output += symStack.pop();
                        output += ' ';
                        break;
                    }
                }
            }
        }
	}
    while (!symStack.isEmpty()) {
        output += symStack.pop();
        output += ' ';
    }

    return output;
}

float infix2Postfix() {
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
    return ans;
    std::cout << "The answer is: " << ans << std::endl;

}