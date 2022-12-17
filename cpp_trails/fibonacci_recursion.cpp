#include <iostream>

//find n-th fibonacci number
int fibonacci(int n) {
    //base case: n == 0
    if (n == 0) { return 0; }
    //base case: n == 1
    else if (n == 1) { return 1; }
    //recursive step
    else { return fibonacci(n-1) + fibonacci(n-2); }
}

//Time Complexity: Exponential O()
//Memory Complexity: 


int main() {
    int result;
    result = fibonacci(40);
    std::cout << result << std::endl;

    return 0;
}