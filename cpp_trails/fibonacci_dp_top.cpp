/* Fibonacci Problem
 * Dynammic Programming
 * Top-down solution
 */


#include <iostream>

#define MAX_LENGTH 10000
long unsigned int fib_arr[MAX_LENGTH] = {0, 1}; //initialize to all 0

long unsigned int fibonacci(int n) {
    // already computed
    if(fib_arr[n] != 0 || n == 0) {
        return fib_arr[n];
    }
    // not computed yet: find answer from top down
    else {
        fib_arr[n] = fibonacci(n-1) + fibonacci(n-2);
        return fib_arr[n];
    }
}

//Time Complexity: Linear
//Memory Complexity: 


int main() {
    int result;
    result = fibonacci(40);
    std::cout << result << std::endl;

    return 0;
}