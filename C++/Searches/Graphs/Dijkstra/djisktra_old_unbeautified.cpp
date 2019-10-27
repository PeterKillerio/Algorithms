#include <vector>
#include <iostream>
#include <queue>

using namespace std;



vector <vector<pair<int,int>>> susedia;
vector <int> nespracovane;
vector <int> spracovane;

#define INF 2000000000

int main(){

    int v;
    int h;

    int a,b,c;

    pair<int,int> d;

    cin >> v >> h;

    for (int i = 0;i < h; i++){
        cin >> a >> b >> c;

        a--;
        b--;

        susedia.resize(v);

        susedia[a].push_back(make_pair(b,c));

        susedia[b].push_back(make_pair(a,c));


    }

    int za,ko;

    cin >> za;
    cin >> ko;

    za--;
    ko--;



    nespracovane.resize(v, INF);
    spracovane.resize(v, -1);


    nespracovane[za] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > nespra;

    nespra.push({0,za});



    while (nespra.size() != 0){

        int num = nespra.top().second;

        nespra.pop();

        spracovane[num] = nespracovane[num];



        for (int j = 0; j < susedia[num].size(); j++) {


            if(spracovane[susedia[num][j].first] == -1){

                int index = susedia[num][j].first;

                int vz = susedia[num][j].second + nespracovane[num];





                if(vz < nespracovane[index]){

                    nespra.push({vz, index});
                    nespracovane[index] = vz;

                }
            }




        }


    }

    cout << spracovane[ko] << endl;




}