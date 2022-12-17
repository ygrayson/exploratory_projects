#include <iostream>

//calculate factorial!
int factorial(int n) {
    //base case: n == 0
    if (n == 0) { return 1; }
    //recursive case: n > 0
    else { return n * factorial(n-1); }
}

//Time Complexity: Linear O(n)
//Memory Complexity: Linear O(n)


int main() {
    int result;
    result = factorial(20);
    std::cout << result << std::endl;

    return 0;
}