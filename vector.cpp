#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int>vec;
    cout<<"size:" <<vec.size()<<endl;
    vec.push_back(34);
    vec.push_back(44);
    vec.push_back(45);
    vec.push_back(67);
    cout<<"after push back="<<vec.size() <<endl;

   vec.pop_back();
   cout<<"after pop back"<<vec.size()<<endl;

    cout<<"front:"<<vec.front() <<endl;
    cout<< "CAPCITY:"<<vec.capacity() <<endl;

    for (int i : vec)
    cout<<i<<endl;

    return 0;
}