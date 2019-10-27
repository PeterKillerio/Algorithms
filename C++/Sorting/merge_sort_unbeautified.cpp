#include <iostream>
#include <vector>
using namespace std;

int size_a;

vector <int> a;
vector <int> ad;

vector<int> merge( vector<int> & u,vector<int> & i){
    unsigned int pocA = 0;
    unsigned int pocB = 0;
    unsigned int mass = (u.size()+ i.size());
    unsigned int index = 0;

    vector <int> c(mass);

    while ((pocA+pocB) != mass){

        if (( pocA < u.size())  &&  (pocB < i.size())){

            if (u[pocA] > i[pocB]){
                c[index] = i[pocB];

                index++;
                pocB++;

            }else {
                c[index] = u[pocA];

                index++;
                pocA++;
            }
        }else{

            if(pocA == u.size()){
                c[index] = i[pocB];

                index++;
                pocB++;


            }else{
                c[index] = u[pocA];

                index++;
                pocA++;
            }
        }
    }
    return c;
}



vector<int> divide_sort(vector<int> & a){

    int velkost;
    velkost = a.size()/2;
    vector <int> b(velkost);

    int druhe = a.size()-velkost;
    vector <int> c(druhe);//

    if (a.size() > 1){

        for (int y = 0;y < velkost; y++){
            b[y] = a[y];
        }

        for (int z = 0;z < druhe; z++){
            if(velkost == druhe){
                c[z] = a[(druhe+z)];
            }else{
                c[z]= a[(druhe-1)+z];
            }
        }

    }else{
        return a;
    }

    vector<int> c2=divide_sort(c);
    vector<int> b2=divide_sort(b);
    return merge(c2,b2);
}

int main() {
    cin >> size_a;

    a.resize(size_a);
    ad.resize(size_a);

    int inputNumber;
    for (int x = 0; x < size_a; x++){
        cin >> inputNumber;
        a[x] = inputNumber;
        ad[x] = inputNumber;
    }

    divide_sort(a);

    return 0;
}