// #include <iostream>
// using namespace std;

// int main(){
//     //     int size =5;
// //     int marks[size];

// //    for(int i=0; i<size; i++){
// //         cin>>marks[i];
// //    }

// //     for(int i=0; i<size; i++){
// //           cout<<marks[i]<<endl;
// //     }
  
//     return 0;
// }





// #include <iostream>
// using namespace std;

// int main(){
    // Q.find smallest number
    // int nums[]={10,20,-3, 60,-40,7};
    // int size = 6;
    // int smallest = INT16_MAX;  

    // for(int i=0; i<size; i++){
    //     if(nums[i]<smallest){
    //         smallest=nums[i];
    //     }
    // }
    // cout<<"smallest:"<<smallest;

        //  OR

    // int nums[]={10,20,-3, 60,-40,7};
    // int size = 6;
    // int smallest = INT16_MAX;  

    // for(int i=0; i<size; i++){
    //     smallest=min(nums[i],smallest) ;
    // }
    // cout<<"smallest:"<<smallest;


    // Q.find heghest number
    // int nums[]={10,20,-3, 60,-40,7};
    // int size = 6;
    // int heighest = INT16_MIN;  

    // for(int i=0; i<size; i++){
    //     if(nums[i]>heighest){
    //         heighest=nums[i];
    //     }
    // }
    // cout<<"heighest:"<<heighest;

                //  OR

    // int nums[]={10,20,-3, 60,-40,7};
    // int size = 6;
    // int heighest = INT16_MIN;  

    // for(int i=0; i<size; i++){
    //     heighest=max(nums[i],heighest) ;
    // }
    // cout<<"heighest:"<<heighest;
//     return 0;
// }




// LINEAR_SEARCH
// #include <iostream>
// using namespace std;

// int linearSearch(int nums[], int sz, int target){
//     for(int i=0; i<sz; i++){
//         if(nums[i]==target){
//             return i;
//         }
//     }
//     return -1;
// }

// int main(){
//   int nums[]={2,3,4,6,7,4};
//   int sz=6;
//   int target = 3;
//   cout<<linearSearch(nums,sz,target);
//     return 0;
// }




// REVERSEARRAY
#include <iostream>
using namespace std;

void reverseArray(int arr[],int sz){
    int start=0;int end=sz-1;
    while(start<end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}


int main(){
    int arr[]={4,2,5,7,9,4,0};
    int sz=7;
    reverseArray(arr,sz);
    for(int i=0; i<sz; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}