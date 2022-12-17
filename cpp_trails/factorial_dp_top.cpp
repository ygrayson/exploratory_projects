/* Factorial Problem
 * Dynammic Programming
 * Top-down solution
 */

#include <iostream>

#define MAX_LENGTH 10000
long unsigned int fact_arr[MAX_LENGTH] = {1}; //initialize to {1,0,0,...}

long unsigned int factorial(int n) {
    // already computed
    if (fact_arr[n] != 0) {
        return fact_arr[n];
    }
    // not computed yet
    else {
        fact_arr[n] = n * factorial(n-1);
        return fact_arr[n];
    }
}

//Time Complexity: Linear O(n)
//Memory Complexity: Linear but bounded O(MAX_LENGTH)


int main() {
    long unsigned int result;
    result = factorial(5); //assume input is always smaller than MAX_LENGTH
    std::cout << result << std::endl;

    return 0;
}