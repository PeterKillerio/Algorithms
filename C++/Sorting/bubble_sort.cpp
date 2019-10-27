#include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int> &v)
{
    for(int i = 0; i < v.size() - 1; ++i)
    {
        for(int j = 0; j < v.size() - i - 1; ++j)
        {
            if(v[j] > v[j+1])
            {
                swap(v[j], v[j+1]);
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> input(n);

    for(int i=0; i<n; ++i)
    {cin >> input[i];}

    BubbleSort(input);

    for(int i=0; i<n; ++i)
    {cout << input[i] << " ";}

    cout << endl;

    return 0;
}