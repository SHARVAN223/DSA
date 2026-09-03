// #include <iostream>
// #include <vector>
// using namespace std;

// int binarySearch(vector<int>num, int target){
//     int st = 0; 
//     int end = num.size()-1;
//     while(st<=end){
//         int mid = (st+end)/2;

//         if (target>num[mid]){
//             st = mid+1;
//         }else if (target<num[mid]){
//             end = mid-1;
//         }else{
//             return mid;
//         }
      
//     }
//     return -1;   

// }



// int binary(vector<int>nums,int target){
//     int st = 0;
//     int end = nums.size()-1;

//     while(st<=end){
//         int mid = st + (end-st)/2;
//         if(target > nums[mid]){
//             st = mid+1;
//         }
//         else if(target <nums[mid]){
//             end = mid-1;
//         }else{
//             return mid;
//         }
//     }
//     return -1;
// }

// int recursionBinary(vector<int>nums,int target, int st , int end){
//     if(st<=end){
//         int mid = st+(end-st)/2;
//         if(target>nums[mid]){
//             return recursionBinary(nums,target, mid+1,end);
//         }else if(target<nums[mid]){
//             return recursionBinary(nums,target, st,mid-1);
//         }else{
//             return mid;
//         }
//     }
//     return -1;
// }

// int main(){
//    vector<int> nums = {-1,0,3,4,5,9,12};
//    int target = 12;
//    cout<<binarySearch(nums,target);
//     // cout<<recursionBinary(nums,target,0,nums.size()-1);
//     return 0;
// }



int n = 8;
int count = 0;

for i in range(1, n+1):
    j = 1
    while j <= n:
        count += 1
        j = j * 2

print(count)