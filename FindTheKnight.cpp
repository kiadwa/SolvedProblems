/**
language: CPP
Count Knight value in a matrix. A value is considered as Knight when it is largest in the row and smallest in the column
Input: First line contains M and NMandN that are the number of rows and columns in matrix (M, N \leq 100)(M,N≤100).

The next MM lines, each is NN non-negative integers aaij (a(aij \leq 1.000≤1.000 with 0 \leq i < M, 0 \leq j < N)0≤i<M,0≤j<N).

Rows are marked from 00 to M-1M−1, and columns are from 00 to N-1N−1.
*/
/** Solution */
#include <iostream>
using namespace std;
bool RowLarge(int x,int y,int nrow,int a[][1000]){
    for(int j = 0; j < nrow; j++){
        if (a[x][j] > a[x][y])
            return false;
    }
    return true;
}

bool ColSmal(int x,int y,int ncol,int a[][1000]){
    for(int i = 0; i < ncol; i++){
        if (a[i][y] < a[x][y])
            return false;
    }
    return true;
}
bool isSaddle(int i, int j, int nrow, int ncol, int a[][1000]){
    if (RowLarge(i,j,nrow,a) && ColSmal(i,j,ncol,a))
        return true;
    return false;
}


int main(){
    int a[1000][1000];
    int n, m;
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }

    int cnt = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if (isSaddle(i, j,n,m, a))
                cnt ++;
        }
    }
    cout << cnt;
}
