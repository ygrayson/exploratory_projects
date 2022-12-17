//Dynammic Programming
//Longest Sequence problem
//Bottom up 


#include <iostream>
using namespace std;

#define M 10

int main() {
    int arr[M] = {3, 10, 2, 1, 20, 2, 9, 12, 8, 14};

    //DP
    int longest[M] = {0};//longest subsequence starting at position i
    
    //loop backward to find longest
    longest[M-1] = 1;
    for(int i = M-2; i >= 0; --i){
        int max = 1;
        for (int j = i+1; j < M; ++j) {
            if(arr[j] > arr[i]) {
                if(longest[j]+1 > max)
                    max = longest[j]+1;
            }
        }
        longest[i] = max;
    }


    int final_longest = 0;
    for(int i = 0; i < M; ++i) {
        cout << longest[i] << endl;
        if(longest[i] > final_longest)
            final_longest = longest[i];
    }
    cout << endl;

    cout << "The overall longest is " << final_longest << endl;

    return 0;
}
