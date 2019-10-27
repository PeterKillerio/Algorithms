#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int main(){
    int v,h;

    cin >> v >> h;

    vector <vector<int>> susedia(v);

    for (int i = 0; i < h ; i++){
        int a,b;
        cin >> a;
        cin >> b;
        a--;
        b--;

        susedia[a].push_back(b);
        susedia[b].push_back(a);

    }

    vector <int> vzdialenost(v,-1);

    queue <int> q;

    int vrchol;
    cin >> vrchol;
    vrchol--;
    q.push(vrchol);

    vzdialenost[vrchol] = 0;
    while (!q.empty()){
        int number = q.front();
        q.pop();

        for (int x = 0; x < susedia[number].size(); x++){
            int check = susedia[number][x];
            if (vzdialenost[check] == -1){
                q.push(check);
                vzdialenost[check] = vzdialenost[number] + 1;
            }



        }



    }


    int kontrol = 0;

    for (int g = 0; g < v; g++){
        if (vzdialenost[g] == 2){
            cout << g+1 << endl;
            kontrol++;
        }
    }
    if (kontrol == 0){
        cout << "-1" << endl;
    }




};



