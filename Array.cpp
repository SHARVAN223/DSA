#include <iostream>
#include <climits>
using  namespace std;

int main(){
    // // int marks[10] = {30,40,50,30,2};
    // int marks[] = {99,30,292,291,9};
    // cout<< sizeof(marks);


// Q. Smallest

  int nums[] = {10,2,17,-9,-7,3};
  int sz = sizeof(nums);

//   int smallest = INT16_MAX;

//   for(int i=0; i<sz; i++){
//     // if(nums[i] < smallest){
//     //     smallest = nums[i];
//     // }
//     smallest = min(nums[i],smallest);
//   }
//   cout<<"smallest:" <<smallest;

//  Q.Largest

// int largest = INT16_MIN;
// for(int i=0; i<sz; i++){
//     if(nums[i]>largest){
//         largest = nums[i];
//     }
// }
// cout<<"largest :" <<largest;

//     return 0;
// }


// Q.Linear Search

// int LinearSearch(int nums[], int sz, int target){
//     for(int i=0; i<sz; i++){
//         if(nums[i] == target){
//             return i;
//         }
//     }
//     return -1;
// }

// int main(){

//     int nums[] = {9,3,4,5,2,8};
//     int sz =sizeof(nums);
//     int target = 8;

//     cout<<LinearSearch(nums,sz,target);
//     return 0;
// }


// Q.Reverse

// int Reverse(int nums[], int sz){
//    int start = 0; 
//    int end = sz-1;

//    while(start<end){
//     swap(nums[start],nums[end]);
//     start++;
//     end--;
//    }
// }

// int main(){

//     int nums[] = {9,3,4,5,2,8};
//     int sz = 6;
       

//    Reverse(nums,sz);

//     for(int i=0; i<sz; i++){
//         cout<<nums[i];
//     }
//     return 0;
}






