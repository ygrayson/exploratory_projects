//Dynammic Programming
//Gold Mining problem
//Top down

#include <iostream>
using namespace std;
#define M 4
#define N 4

// small helper function for max of 3 nums
int max_int(const int a, const int b, const int c){
    int max = a;
    if (b > max){ max = b; }
    if (c > max){ max = c; }
    return max;
}


int optimal_amount(const int gold_mine[M][N], int start_pos[]) {
    static int optimal_gold[M][N] = {{0}}; //2d array to keep track optimal amount

    int row = start_pos[0];
    int colomn = start_pos[1];

    for(int j = N-1; j >= 0; j--){
        for (int i = M-1; i >= 0; i--){
            //right-most colomn
            if(j == N-1)
                optimal_gold[i][j] = gold_mine[i][j];
            //non right-most colomn
            else
                optimal_gold[i][j] = gold_mine[i][j] + max_int(optimal_gold[i][j+1], 
                                                               optimal_gold[max(0, i-1)][j+1], 
                                                               optimal_gold[min(M-1, i+1)][j+1]); } }
    return optimal_gold[row][colomn];
}


int main() {
/*    const int gold_mine_1[M][N] = {{1,2,3,4,5},
                                {2,3,4,5,6},
                                {5,3,6,8,5},
                                {7,4,2,6,9},
                                {1,1,1,1,1}};

    const int gold_mine_2[M][N] = {{1, 3, 3},
                                {2, 1, 4},
                                {0, 6, 4}};
*/
    const int gold_mine_3[M][N] = {{1, 3, 1, 5},
                                    {2, 2, 4, 1},
                                    {5, 0, 2, 3},
                                    {0, 6, 1, 2}};

    int start_pos_1[2] = {2, 0}; //second entry must be 0 (left-most colomn)
    int start_pos_2[2] = {1, 0};
    int start_pos_3[2] = {2, 0};

    int max_gold_1, max_gold_2, max_gold_3;

//    max_gold_1 = optimal_amount(gold_mine_1, start_pos_1);
//    max_gold_2 = optimal_amount(gold_mine_2, start_pos_2);
    max_gold_3 = optimal_amount(gold_mine_3, start_pos_3);
    std::cout << max_gold_3 << std::endl;

    return 0;
}