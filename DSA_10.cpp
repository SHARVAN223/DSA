#include <iostream>
using namespace std;

int main(){
    int arr[5] = {1,2,3,4,5};
    int n = 5;

    int ms = INT16_MIN;
    for(int st = 0; st<n; st++){
       int cs = 0;
        for(int end = st; end<n; end++){
            cs += arr[end];
             ms = max(cs,ms);
        }
    }
    cout<<"max:"<< ms<<endl;

    return 0;
}