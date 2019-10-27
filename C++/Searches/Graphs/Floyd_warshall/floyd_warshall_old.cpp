#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector <vector<pair<int,bool>>> pole;
vector <vector<int>> path;

void floyd(){
    for (int i = 0; i < pole.size(); ++i) {
        for (int j = 0; j < pole.size(); ++j) {
            for (int k = 0; k < pole.size(); ++k) {
                if (pole[j][i].first + pole[i][k].first < pole[j][k].first){
                    pole[j][k].first = pole[j][i].first + pole[i][k].first;
                }
            }
        }
    }
}

int main() {
    int n,m;
    cin >> n >> m;

    pole.resize(n);
    path.resize(n);
    for (int i = 0; i < n; ++i) {
        pole[i].resize(n);
        path[i].resize(n);
    }

    // ADDING WEIGHTS TO THE "ROADS" FOR 4X4 MATRIX
    // EXAMPLE INPUT MATRIX
    // (row position - from which node we are connecting)
    // (column position - to which node we are connecting)
    // (Value on that position represents Lenght of that connection and the algorithm finds the shortest path)

    pole[0][0].first = {0};
    pole[0][1].first = {1};
    pole[0][2].first = {100000};
    pole[0][3].first = {100000};

    pole[1][0].first = {100000};
    pole[1][1].first = {0};
    pole[1][2].first = {2};
    pole[1][3].first = {100000};

    pole[2][0].first = {2};
    pole[2][1].first = {5};
    pole[2][2].first = {0};
    pole[2][3].first = {100000};

    pole[3][0].first = {100000};
    pole[3][1].first = {10};
    pole[3][2].first = {2};
    pole[3][3].first = {0};

    //PRINTING OUT THE MATRIX BEFORE FLOYD ALGORITHM

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            cout << pole[k][i].first << " ";
        }cout << endl;
    }cout << endl;

    floyd();

    //PRINTING OUT THE MATRIX AFTER FLOYD ALGORITHM
    // Columns indicate to which node we are connecting
    // Rows indicate from which node we are connecting
    // The shortest path is on the position ROWxCOLUMN
    // For example, the shortest path from node 0 to 2 is 3
    // because the shortest path leads through node 1
    // and thus 0->1 is length of 1 and from 1-> is lenght of 2 = 3

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            cout << pole[k][i].first << " ";
        }cout << endl;
    }
    return 0;
}