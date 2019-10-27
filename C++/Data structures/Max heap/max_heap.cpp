// INPUT FORMAT
// I. number of operations you want to do
// II. your operation, write "1" if you want to insert a number and then write the number (f.e.  1 25)
// III. if you dont want to add number but you want to delete the biggest number type 0


#include <iostream>
#include <vector>
using namespace std;

void swap(int index1,int index2,vector<int> &arrayInn){
    int cislo = arrayInn[index2];
    arrayInn[index2] = arrayInn[index1];
    arrayInn[index1] = cislo;
}

void topdel(vector<int>& arrayInn){
    if(arrayInn.size()==1){
        return;
    }

    swap(1, arrayInn.size()-1,arrayInn);

    // Deleting
    cout << "Deleting: " << arrayInn[arrayInn.size()-1] << endl;

    arrayInn.pop_back();

    int parent,child;

    parent = 1;
    child = 2*parent;

    while (parent*2 < arrayInn.size()){

        if(arrayInn.size() == (2*parent)+1){

            if (arrayInn[child] > arrayInn[parent]){
                swap(parent,child,arrayInn);

                parent = child;
                child = parent*2;
            }else{
                return;
            }
        }else{

            if(arrayInn[child] > arrayInn[child+1]){


                if (arrayInn[child] > arrayInn[parent]){

                    swap(parent,child,arrayInn);
                    parent = child;
                    child = parent*2;

                }else{
                    return;
                }

            }else {
                if(arrayInn[child+1] > arrayInn[parent]){
                    swap(parent,child+1,arrayInn);
                    parent = child+1;
                    child = parent*2;
                }else {
                    return;
                }
            }
        }
    }
}

void addnum(int number,vector<int>& asd){
    int child,fath;

    asd.push_back ( number );

    //adding
    cout <<"adding: " << number << endl;

    child = asd.size()-1;
    fath = (child/2);

    while((child > 1)&&(asd[child] > asd[fath])){
        swap(child,fath,asd);

        child = fath;
        fath = (child/2);
    }
}
int main() {
    int howMany, operation;

    cin >> howMany;
    vector <int> arrayA(1);
    arrayA[0] = 0;

    for(int x = 0; x < (howMany); x++){

        cin >> operation;

        if (operation == 1){

            int number;
            cin >> number;

            addnum(number,arrayA);

        }else{
            if(arrayA.size() > 1) {

                topdel(arrayA);
            }
        }
    }
    return 0;
}