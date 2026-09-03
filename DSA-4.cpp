// #include <iostream>
// #include <vector>
// using namespace std;


// vector <int> pairSum( vector<int> nums,int target){
//     vector <int> ans;
//     int n = nums.size();

    // for (int i=0; i<n; i++){
    //     for (int j=i+1; j<n; j++){
    //         if(nums[i] + nums[j] == target){
    //             ans.push_back(i);
    //             ans.push_back(j);
    //             return ans;
    //         }
    //     }
    // }
    // return ans;


    // OR



//     int i=0, j=n-1;

//     while(i<j){
//         int pairSum = nums[i] + nums[j];

//         if(pairSum>target){
//             j--;
//         }else if(pairSum<target){
//             i++;
//         }else{
//             ans.push_back(i);
//             ans.push_back(j);
//             return ans;
//         }
//     }
//     return ans;
// }

// int main(){
//     vector<int> nums = {2,7,11,15};
//     int target = 13;

//     vector <int> ans= pairSum(nums,target);
//     cout<<ans[0]<<", "<<ans[1]<<endl;
//     return 0;
// }



// # MAJORITY ELEMENT


#include <iostream>
#include <vector>
using namespace std;


int main(){
    // vector <int> nums = {2,2,1,1,1};
    // int n = nums.size();

    // for(int val : nums){
    //     int frequency = 0;
    //     for (int el : nums){
    //         if (el == val){
    //             frequency++;
    //         }
    //     }
    //     if(frequency>n/2){
    //         cout<<val;
    //         return 0;
    //     }
    // }


    int a=10;
    int* ptr = &a;
    cout<<ptr<<endl;
    ptr++;
    cout<<ptr<<endl;
    // int** pareptr = &ptr;
    // cout<<ptr<<endl;
    // cout<<**pareptr<<endl;
}