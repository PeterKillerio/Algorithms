// YEARS OLD IMPLEMENTATION
// This particular code takes an input for example names of the cities
// lets say we create 5 nodes
// each node is going to correspond with a city
// each new input ,totally (5 inputs), is going to look like
// this : "city city" f.e "Prague Paris" after this
// we create a connection between those two nodes and program is going to write
// out number of new pairs that have been created ("connected")
// EXAMPLE INPUT/OUTPUT
// I:5
// I:Prague Paris
// O:1
// I:Berlin Bratislava
// O:1
// I:Paris Amsterdam
// O:2
// I:Prague Bratislava
// O:6
// I:Prague Amsterdam
// O:0

#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

vector <pair<int,int>> parrent;
vector <int> siz;
map <string,int> mymap;

int find_parrent(int x){
    if (parrent[x].first == x){
        return x;
    }else{
        parrent [x].first = find_parrent(parrent[x].first);
        return parrent[x].first;
    }
}

void uni(int x,int y){
    int p_x = find_parrent(x);
    int p_y = find_parrent(y);

    if (p_x != p_y){
        int aa,bb,vv;
        aa = parrent[p_x].second;
        bb = parrent[p_y].second;
        vv = aa*bb;

        if (siz[p_x] > siz[p_y]){
            parrent[p_y].first = p_x;
            parrent[p_x].second = parrent[p_x].second + parrent[p_y].second;

        }else if (siz[p_x] < siz[p_y]){
            parrent[p_x].first = p_y;
            parrent[p_y].second = parrent[p_y].second + parrent[p_x].second;
        }else{
            parrent[p_x].first = p_y;
            parrent[p_y].second = parrent[p_x].second + parrent[p_y].second;
            siz[p_y]++;
        }

        cout << vv << endl;
    }else{
        cout << 0 << endl;
    }
}

int main() {

    int n;
    int index = 0;
    cin >> n;

    parrent.resize(n*2);
    siz.resize(n*2);

    for (int i = 0;i < (2*n); i++){
        parrent[i].first = i;
        parrent[i].second = 1;
        siz[i] = 1;
    }

    for (int w = 0; w < n; w++){
        string o,l;
        cin >> o >> l;

        if (mymap.count(o) == 0){
            mymap[o] = index;
            index++;
        }
        if (mymap.count(l) == 0){
            mymap[l] = index;
            index++;
        }

        int xx = mymap[o];
        int yy = mymap[l];

        uni(xx,yy);
    }

    return 0;
}