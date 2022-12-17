/* Factorial Problem
 * Dynammic Programming
 * Bottom-up solution
 */

#include <iostream>
#define MAX_LENGTH 10000

long unsigned int factorial(int n) {
    long unsigned int fact_arr[MAX_LENGTH] = {0}; //initialize to all 0

    fact_arr[0] = 1;
    for (int i = 1; i < n+1; i++) {
        fact_arr[i] = fact_arr[i-1] * i;
    }

    return fact_arr[n];
}

//Time Complexity: Linear O(n)
//Memory Complexity: Linear but bounded O(MAX_LENGTH)


int main() {
    long unsigned int result;
    result = factorial(5); //assume input is always smaller than MAX_LENGTH
    std::cout << result << std::endl;

    return 0;
}