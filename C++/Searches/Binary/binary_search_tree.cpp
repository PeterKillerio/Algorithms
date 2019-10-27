#include <iostream>
using namespace std;

int binarySearch(int A[],int n,int x){
    int low = 0,high = n-1;
    while(low <= high){
        int mid = (low+high)/2;
        if(A[mid]== x)return 1;
        else if (x < A[mid]) high = mid - 1;
        else low = mid+1;
    }
    return 0;
}

// INPUT FORMAT:
// I. size x of numbers you want to add to the tree
// II. your x numbers
// III. y number of questions you want to "ask" the tree
// IV. you y number of questions and for each you receive Yes or No

int main(int argc, char **argv) {
    int size,questions;

    cin >> size;
    int Ar[size];

    for (int i = 0; i < size; i++) {
        int a;
        scanf("%d",&a);
        Ar[i] = a;
    }

    cin >> questions;

    for (int j = 0; j < questions; j++) {
        int number,c;

        scanf("%d",&number);

        if (binarySearch(Ar,size,number)){
            printf("Y\n");
        }else{
            printf("N\n");
        }
    }

    return 0;
}
