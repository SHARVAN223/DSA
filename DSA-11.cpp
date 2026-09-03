#include <iostream>
#include <vector>
using namespace std;

vector <int> PairSum(vector<int> nums , int target){
    vector<int> ans;
    int n = nums.size();

    // BRUTE approach
    // for(int i=0; i<n; i++){
    //     for(int j = i+1; j<n; j++){
    //         if(nums[i]+nums[j] == target){
    //             ans.push_back(i);
    //             ans.push_back(j);
    //             return ans;
    //         }
    //     }
    // }
    // return ans;


    // OPTIMIZE APPROACH

    int i =0; 
    int j = n-1;

    while(i<j){
        int ps = nums[i] + nums[j];
        if(ps>target){
            j--;
        }else if(ps<target){
            i++;
        }else{
            ans.push_back(i);
            ans.push_back(j);
            return ans;
        }
    }
    return ans;
}

int main(){
    vector<int> nums = {2,4,6,7};
    int target = 13;

    vector<int> ans= PairSum(nums,target);
    cout<<ans[0] <<", " <<ans[1];
    
    return 0;
}