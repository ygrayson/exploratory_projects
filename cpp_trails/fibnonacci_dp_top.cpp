/* Fibonacci Problem
 * Dynammic Programming
 * Top-down solution
 */

#include <iostream>

#define MAX_LENGTH 10000
int fib_arr[MAX_LENGTH] = {0, 1}; //initialize to all 0

int fibonacci(int n) {
    // base case: fib(0) = 0
    if (n == 0) { return 0; }
    //already computed
    else if (fib_arr[n] != 0) { return fib_arr[n]; }
    // not computed: compute from top down
    else {
        fib_arr[n] = fibonacci(n-1) + fibonacci(n-2);
        return fib_arr[n];
    }
}

//Time Complexity: Linear
//Memory Complexity: 


int main() {
    int result;
    result = fibonacci(6);
    std::cout << result << std::endl;

    return 0;
}