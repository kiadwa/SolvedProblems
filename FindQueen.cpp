'''language: CPP
problem description: Count "queen" values in a square matrix.
                     A value is considered as a queen when it is the largest number in the row,
                     the column and 2 diagonals passing through it. 
Input:   First line is NN that is the number of rows and columns of a quare matrix (N \leq 100)(N≤100).

The next NN following lines: each is NN positive integers aaij (aaij \leq 1.000≤1.000 with 0 \leq i, j < N0≤i,j<N).

Rows are marked from 00 to N-1N−1, and columns are from 00 to N-1N−1.                 
'''

''' Solution '''

#include <iostream>
using namespace std;
bool columnMax(int x, int y, int n, int a[][100]){
  for( int i = 0; i < n; i++){
      int k = a[x][i];
      int f = a[x][y];
      if (a[x][i] > a[x][y])
      return false;
  }
  return true;
}

bool rowMax(int x, int y, int n, int a[][100]){
  for(int i = 0; i < n; i++){
      int k = a[i][y];
      int f = a[x][y];
    if (a[i][y] > a[x][y])
      return false;
  }
  return true;
}

bool lrdiagMax(int x, int y, int n, int a[][100]){
  int r = x;
  int c = y;
  while ((c < n) && (r < n)){
      bool z = (c < n && r < n);
    int k = a[r][c];
    int f = a[x][y];
    if (a[r][c] > a[x][y])
      return false;
    r++;
    c++;
  }
  r = x;
  c = y;
  while ((r >= 0) && (c >= 0)){
      bool z = ( r>=0 && c>=0 );
      int k = a[r][c];
      int f = a[x][y];
    if (a[r][c] > a[x][y])
      return false;
    r--;
    c--;
  }
  return true;
}

bool rldiagMax(int x, int y, int n, int a[][100]){
  int r = x;
  int c = y;
  while ((r >= 0) && (c < n)){
      int k = a[r][c];
      int f = a[x][y];
    if (a[r][c] > a[x][y])
      return false;
    r--;
    c++;
  }
  r = x;
  c = y;
  while ((r < n) && (c >= 0)){
      int k = a[r][c];
      int f = a[x][y];
    if (a[r][c] > a[x][y])
      return false;
  	r++;
    c--;
  }
  return true;
}

int main(){
  int a[100][100];
  int n;
  cin >> n;
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      cin >> a[i][j];
    }
  }
  int cnt = 0;
  for (int i =0; i < n; i++){
    for(int j = 0; j < n; j++){
      if ( columnMax(i,j,n,a) && rowMax(i,j,n,a) && lrdiagMax(i,j,n,a) && rldiagMax(i,j,n,a)){
        cnt ++;
      	}
    }
  }
  cout << cnt;
}







