#include <vector>
#include <iostream>

using namespace std;

int list;
vector <bool> visited;
vector <vector<int>> neighbours;

void DFS(int x){
    visited[x] = true;
    for (int f = 0; f < neighbours[x].size();f++){
        int number = neighbours[x][f];
        if (visited[number] == false){
            DFS(number);
        }
    }

    if (neighbours[x].size()== 1 and x!=0){
        list++;
    }
}


int main(){
    int v;

    cin >> v;

    neighbours.resize(v);

    for (int i = 0; i < (v-1) ; i++){
        int a,b;
        cin >> a;
        cin >> b;
        a--;
        b--;

        neighbours[a].push_back(b);
        neighbours[b].push_back(a);
    }

    visited.resize(v,false);

    DFS(0);

    cout << list << endl;
}


